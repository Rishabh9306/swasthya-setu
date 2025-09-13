# ======================================================================================
# MODIFICATIONS FOR TRANSLATION AND GRAMMAR CORRECTION
#
# 1. New helper function `utter_translated_message` is added to handle response translation.
# 2. All Action classes are updated to:
#    a. Call `normalize_for_rasa` to detect the user's language.
#    b. Store the detected language in the `language` slot.
#    c. Use `utter_translated_message` instead of `dispatcher.utter_message` to send translated responses.
# 3. The `run_kb_pipeline` function is updated to use normalized text for lookups.
#
# ACTION REQUIRED: Add the 'language' slot to your domain.yml file.
# ======================================================================================
from typing import Any, Text, Dict, List, Optional
import re
import requests
import logging
import json
import os
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

# --- All your existing imports and initializations ---
from knowledge_base.fallback_system import GeoFallback, SemanticKB, HealthGlossary
from knowledge_base.vector_store import load_vector_store, search_corpus

geo_fallback_handler = GeoFallback()
semantic_kb_handler = SemanticKB()
health_glossary_handler = HealthGlossary()
load_vector_store()
MEDICINE_API_URL = "http://localhost:8000"
TRANSLATION_API_URL = "http://localhost:8001"

# ============================================================================
# TRANSLATION AND NORMALIZATION FUNCTIONS
# ============================================================================

def normalize_for_rasa(raw_text: str) -> Dict[Text, Any]:
    """
    Calls the /normalize endpoint of our translation service.
    Returns a dictionary with the normalized English and detected language.
    """
    # If input is empty or None, return default
    if not raw_text:
        return {"text": raw_text, "language": "en"}
    try:
        response = requests.post(f"{TRANSLATION_API_URL}/normalize", json={"text": raw_text}, timeout=10.0)
        response.raise_for_status()
        data = response.json()
        return {
            "text": data.get("normalized_english", raw_text),
            "language": data.get("detected_language", "en")
        }
    except requests.exceptions.RequestException as e:
        logging.error(f"Could not connect to translation service at '{TRANSLATION_API_URL}'. Error: {e}")
        # Fail-safe: if the service is down, process the original text in English.
        return {"text": raw_text, "language": "en"}

def translate_for_user(english_text: str, language: str) -> str:
    """
    MODIFIED: Calls the /translate_back endpoint if the detected language
    was not English. Now supports 'odia' and 'hindi'.
    """
    # Only translate if the user's original language was Odia or Hindi.
    if language in ["or", "hi", "odia", "hindi"]: # Supporting both long and short codes
        try:
            # NOTE: This assumes the translation service at /translate_back
            # can handle a 'target_language' parameter (e.g., 'or' for odia, 'hi' for hindi).
            lang_code_map = {"odia": "or", "hindi": "hi", "or": "or", "hi": "hi"}
            target_code = lang_code_map.get(language)

            if not target_code:
                return english_text

            response = requests.post(
                f"{TRANSLATION_API_URL}/translate_back",
                # Sending the target language code to the service
                json={"text": english_text, "target_language": target_code},
                timeout=10.0
            )
            response.raise_for_status()
            data = response.json()
            return data.get("translated_text", english_text)
        except requests.exceptions.RequestException as e:
            logging.error(f"Could not connect to translation service for translate_back. Error: {e}")

    # Default: return the original English text
    return english_text

def utter_translated_message(
    dispatcher: CollectingDispatcher,
    language: str,
    domain: Dict[Text, Any],
    template: Optional[Text] = None,
    text: Optional[Text] = None,
    **kwargs: Any
):
    """
    NEW: A helper function to construct the English message from text or a template,
    translate it if the language is not 'en', and then dispatch the final message.
    """
    english_text = ""
    if text:
        english_text = text
    elif template:
        try:
            # Fetch the first response for the given template and format it.
            # This simplification doesn't handle rich responses like buttons or images.
            template_response = domain["responses"][template][0]
            if "text" in template_response:
                english_text = template_response["text"].format(**kwargs)
            else:
                # If there's no text (e.g., just buttons), pass through without translation.
                dispatcher.utter_message(template=template, **kwargs)
                return
        except (KeyError, IndexError, TypeError) as e:
            logging.error(f"Error processing template '{template}': {e}. Sending original template.")
            # Fallback for safety
            dispatcher.utter_message(template=template, **kwargs)
            return

    if not english_text:
        logging.warning(f"No text generated for template '{template}' or text argument was empty.")
        if template: # As a fallback, try sending the original template
            dispatcher.utter_message(template=template, **kwargs)
        return

    # Translate the final English text and send it.
    final_text = translate_for_user(english_text, language)
    dispatcher.utter_message(text=final_text)


# ============================================================================
# VACCINATION AND OUTBREAK JSON FALLBACK SYSTEM (Unchanged)
# ============================================================================
VACCINE_SCHEDULE_DATA = []
try:
    schedule_path = os.path.join(os.path.dirname(__file__), '..', 'vaccination_schedule.json')
    with open(schedule_path, 'r', encoding='utf-8') as f:
        VACCINE_SCHEDULE_DATA = json.load(f)
    logging.info("Successfully loaded local vaccination_schedule.json")
except Exception as e:
    logging.error(f"FATAL ERROR: Failed to load vaccination_schedule.json. Error: {e}")

def get_schedule_from_json(age_input: str) -> Optional[str]:
    # This function's logic remains unchanged.
    if not VACCINE_SCHEDULE_DATA or not age_input: return None
    age_in_months: Any = -1
    age_display = age_input
    if "pregnant" in age_input.lower():
        age_in_months = "pregnant"
        age_display = "expectant mothers"
    else:
        numbers = re.findall(r'\d+', age_input)
        if numbers:
            num = int(numbers[0])
            if "year" in age_input.lower(): age_in_months = num * 12
            elif "month" in age_input.lower(): age_in_months = num
            else: age_in_months = num * 12 if num > 1 else num
    schedule_found = None
    if age_in_months == "pregnant":
        schedule_found = next((item for item in VACCINE_SCHEDULE_DATA if item.get("age_group") == "pregnant"), None)
    elif isinstance(age_in_months, int) and age_in_months >= 0:
        eligible_schedules = sorted(
            [s for s in VACCINE_SCHEDULE_DATA if "age_months" in s and s["age_months"] <= age_in_months],
            key=lambda x: x['age_months']
        )
        if eligible_schedules:
            schedule_found = eligible_schedules[-1]
    if schedule_found and schedule_found.get("vaccines"):
        response_lines = [f"Based on the National Immunisation Schedule, here are the key vaccines for **{age_display}**:"]
        for vaccine in schedule_found["vaccines"]:
            response_lines.append(f"• **{vaccine['name']}** – {vaccine['description']}")
        response_lines.append("\n**IMPORTANT:** This is a general guideline. Please consult your local ASHA worker.")
        return "\n".join(response_lines)
    return None

OUTBREAK_DATA = []
try:
    outbreak_path = os.path.join(os.path.dirname(__file__), '..', 'idsp_outbreaks.jsonl')
    with open(outbreak_path, 'r', encoding='utf-8') as f:
        for line in f:
            OUTBREAK_DATA.append(json.loads(line))
    logging.info(f"Successfully loaded {len(OUTBREAK_DATA)} records from idsp_outbreaks.jsonl")
except Exception as e:
    logging.error(f"FATAL ERROR: Failed to load idsp_outbreaks.jsonl. Outbreak fallback will not work. Error: {e}")

def get_outbreaks_from_json(location_input: str) -> Optional[str]:
    # This function's logic remains unchanged.
    if not OUTBREAK_DATA or not location_input: return None
    location_lower = location_input.lower()
    results = [
        record for record in OUTBREAK_DATA
        if location_lower in record.get("district", "").lower() or
        location_lower in record.get("state", "").lower()
    ]
    if not results:
        return f"No recent outbreak data is available for {location_input.title()} in our records."
    results.sort(key=lambda x: x.get("district", ""))
    response_lines = [f"Recent health alerts for {location_input.title()}:"]
    for report in results:
        summary = (
            f"• {report.get('disease', 'N/A')} in {report.get('district', 'N/A')}: "
            f"{report.get('cases', 0)} cases, {report.get('deaths', 0)} deaths. "
            f"Status: {report.get('status', 'N/A')}."
        )
        response_lines.append(summary)
    response_lines.append("\nSource: Integrated Disease Surveillance Programme (IDSP). Please consult official MoHFW channels for the latest information.")
    return "\n".join(response_lines)

# ============================================================================
# KNOWLEDGE BASE PIPELINE (MODIFIED)
# ============================================================================

def run_kb_pipeline(
    dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any],
    normalized_text: str,
    language: str
) -> bool:
    """
    MODIFIED: A reusable function to run the full Knowledge Base pipeline.
    Now accepts normalized_text for lookups and language for response translation.
    """
    glossary_result = health_glossary_handler.lookup(normalized_text)
    if glossary_result:
        term, definition_dict = glossary_result
        definition = definition_dict.get('def_en', 'No definition found.')
        reference = definition_dict.get('reference', 'Source not available')
        utter_translated_message(
            dispatcher, language, domain,
            template="utter_found_in_glossary",
            term=term.upper(),
            definition=definition,
            reference=reference
        )
        return True

    kb_result = semantic_kb_handler.search(normalized_text)
    if kb_result:
        answer = kb_result.get('answer_en', "I found information but couldn't format it.")
        reference = kb_result.get('reference', 'Source not available')
        utter_translated_message(
            dispatcher, language, domain,
            template="utter_found_in_kb",
            answer=answer,
            reference=reference
        )
        return True

    return False

# ============================================================================
# RASA ACTIONS (MODIFIED FOR TRANSLATION)
# ============================================================================

class ActionDefaultFallbackOrchestrator(Action):
    """MODIFIED: Handles fallback with translation and normalization."""
    def name(self) -> Text: return "action_default_fallback_orchestrator"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message.get('text')
        normalized_data = normalize_for_rasa(user_input)
        language = normalized_data.get("language", "en")
        normalized_text = normalized_data.get("text", user_input)

        corpus_result = search_corpus(normalized_text)
        if corpus_result:
            translated_result = translate_for_user(corpus_result, language)
            dispatcher.utter_message(text=translated_result)
            return [SlotSet("language", language)]

        if run_kb_pipeline(dispatcher, tracker, domain, normalized_text, language):
            return [SlotSet("language", language)]

        utter_translated_message(dispatcher, language, domain, template="utter_fallback")
        return [SlotSet("language", language)]


class ValidateVaccinationForm(FormValidationAction):
    """Validation logic for the vaccination_form. (Unchanged)"""
    def name(self) -> Text: return "validate_vaccination_form"
    async def validate_age(self, slot_value: Any, d: CollectingDispatcher, t: Tracker, dom: DomainDict) -> Dict[Text, Any]:
        return {"age": slot_value} if slot_value else {"age": None}
    async def validate_location(self, slot_value: Any, d: CollectingDispatcher, t: Tracker, dom: DomainDict) -> Dict[Text, Any]:
        return {"location": slot_value} if slot_value else {"location": None}


class ActionAskVaccinationSchedule(Action):
    """MODIFIED: Handles vaccination schedule requests with output translation."""
    def name(self) -> Text: return "action_ask_vaccination_schedule"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get language from slot, which should have been set by a previous action.
        # Fallback to 'en' if not set.
        language = tracker.get_slot("language") or "en"

        if tracker.get_intent_of_latest_message() == "ask_vaccination_schedule_pregnant":
            schedule_string = get_schedule_from_json("pregnant")
            if schedule_string:
                translated_schedule = translate_for_user(schedule_string, language)
                dispatcher.utter_message(text=translated_schedule)
            else:
                utter_translated_message(dispatcher, language, domain, text="I can provide vaccine info for pregnant women, but couldn't retrieve it now. Please consult your doctor.")
            return []

        age = tracker.get_slot("age")
        location = tracker.get_slot("location")
        age_text = age if age else "the person"
        if age and ("year" in age.lower() or "month" in age.lower()) and "old" not in age.lower():
            age_text = f"{age} old"

        api_works = False
        if api_works:
            utter_translated_message(dispatcher, language, domain, template="utter_vaccination_schedule_api", age=age_text, location=location)
        else:
            schedule_string = get_schedule_from_json(age)
            if schedule_string:
                translated_schedule = translate_for_user(schedule_string, language)
                dispatcher.utter_message(text=translated_schedule)
            else:
                utter_translated_message(dispatcher, language, domain, template="utter_vaccination_schedule_fallback", age=age_text, location=location)

        return [SlotSet("age", None), SlotSet("location", None)]


class ActionHandleDiseaseQuery(Action):
    """MODIFIED: Handles disease queries with translation and normalization."""
    def name(self) -> Text: return "action_handle_disease_query"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message.get('text')
        normalized_data = normalize_for_rasa(user_input)
        language = normalized_data.get("language", "en")
        normalized_text = normalized_data.get("text", user_input)

        disease = next(tracker.get_latest_entity_values("disease"), None)
        latest_intent = tracker.get_intent_of_latest_message()

        if disease:
            disease_key = disease.lower().replace(" ", "").replace("-", "")
            template_map = {"ask_disease_info": f"utter_disease_info_{disease_key}", "ask_symptoms": f"utter_symptoms_{disease_key}", "ask_prevention": f"utter_prevention_{disease_key}"}
            template_name = template_map.get(latest_intent)
            if template_name and template_name in domain.get("responses", {}):
                utter_translated_message(dispatcher, language, domain, template=template_name)
                return [SlotSet("language", language)]

        corpus_result = search_corpus(normalized_text)
        if corpus_result:
            translated_result = translate_for_user(corpus_result, language)
            dispatcher.utter_message(text=translated_result)
            return [SlotSet("language", language)]

        if not run_kb_pipeline(dispatcher, tracker, domain, normalized_text, language):
            utter_translated_message(dispatcher, language, domain, template="utter_disease_guidelines_fallback")

        return [SlotSet("language", language)]


class ActionAskEmergencyContacts(Action):
    """MODIFIED: Handles emergency contact requests with output translation."""
    def name(self) -> Text: return "action_ask_emergency_contacts"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message.get('text', '').strip()
        normalized_data = normalize_for_rasa(user_input)
        language = normalized_data.get("language", "en")

        pincode = tracker.get_slot("pincode") or next(tracker.get_latest_entity_values("pincode"), None)
        intent_name = tracker.latest_message['intent'].get('name')

        if intent_name == "provide_pincode" and re.fullmatch(r'\d{6}', user_input):
            contacts = geo_fallback_handler.get_contacts(user_input)
            if contacts:
                # Geo-fallback provides its own translations, so we handle it directly.
                contact_info = contacts.get('contact_en', 'N/A')
                if language == 'or':
                    contact_info = contacts.get('contact_odia', contact_info)
                dispatcher.utter_message(text=contact_info)
            else:
                utter_translated_message(dispatcher, language, domain, template="utter_pincode_not_found", pincode=user_input)
            return [SlotSet("pincode", None), SlotSet("language", language)]

        if pincode:
            api_works = False
            if api_works:
                utter_translated_message(dispatcher, language, domain, template="utter_emergency_contacts_api", pincode=pincode)
            else:
                utter_translated_message(dispatcher, language, domain, template="utter_emergency_contacts_fallback", pincode=pincode)
            return [SlotSet("pincode", None), SlotSet("language", language)]

        utter_translated_message(dispatcher, language, domain, template="utter_ask_pincode")
        return [SlotSet("language", language)]


class ActionAskOutbreakAlerts(Action):
    """MODIFIED: Handles outbreak alerts with output translation."""
    def name(self) -> Text: return "action_ask_outbreak_alerts"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message.get('text')
        normalized_data = normalize_for_rasa(user_input)
        language = normalized_data.get("language", "en")

        location = next(tracker.get_latest_entity_values("location"), None)

        if not location:
            utter_translated_message(dispatcher, language, domain, template="utter_ask_location_outbreak")
            return [SlotSet("language", language)]

        api_works = False
        if api_works:
            utter_translated_message(dispatcher, language, domain, template="utter_outbreak_alerts_api", location=location)
        else:
            outbreak_string = get_outbreaks_from_json(location)
            if outbreak_string:
                translated_outbreak = translate_for_user(outbreak_string, language)
                dispatcher.utter_message(text=translated_outbreak)

        return [SlotSet("language", language)]


class ActionMedicineLookup(Action):
    """MODIFIED: Handles medicine lookups with output translation."""
    def name(self) -> Text: return "action_medicine_lookup"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message.get('text')
        normalized_data = normalize_for_rasa(user_input)
        language = normalized_data.get("language", "en")

        intent_name = tracker.latest_message['intent'].get('name')
        try:
            if intent_name == "ask_medicine_info":
                medicine_name = next(tracker.get_latest_entity_values("medicine"), None)
                if not medicine_name:
                    utter_translated_message(dispatcher, language, domain, template="utter_ask_for_medicine")
                    return [SlotSet("language", language)]
                response = requests.get(f"{MEDICINE_API_URL}/info", params={"name": medicine_name})
                response.raise_for_status()
                # Translate API response
                summary = response.json().get("summary", "No information found.")
                translated_summary = translate_for_user(summary, language)
                dispatcher.utter_message(text=translated_summary)

            elif intent_name == "compare_medicines":
                entities = list(tracker.get_latest_entity_values("medicine"))
                if len(entities) < 2:
                    utter_translated_message(dispatcher, language, domain, text="To compare, please provide two medicine names, like 'Pan-D vs Pan-40'.")
                    return [SlotSet("language", language)]
                response = requests.get(f"{MEDICINE_API_URL}/compare", params={"med1": entities[0], "med2": entities[1]})
                response.raise_for_status()
                # Translate API response
                summary = response.json().get("summary", "Could not compare the medicines.")
                translated_summary = translate_for_user(summary, language)
                dispatcher.utter_message(text=translated_summary)

        except requests.exceptions.RequestException as e:
            logging.error(f"Could not connect to the Medicine API: {e}")
            utter_translated_message(dispatcher, language, domain, template="utter_api_down_medicine")

        return [SlotSet("language", language)]