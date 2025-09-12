# actions/actions.py (Definitive Version with Integrated JSON Fallback)

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

# ============================================================================
# NEW: VACCINATION JSON FALLBACK SYSTEM
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
    """
    Parses a user's age, finds the latest eligible schedule from JSON,
    and formats it into a user-friendly string.
    """
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
        # --- CRITICAL BUG FIX FOR 10-MONTH-OLD ---
        # Sort schedules to ensure we process them in order of age
        eligible_schedules = sorted(
            [s for s in VACCINE_SCHEDULE_DATA if "age_months" in s and s["age_months"] <= age_in_months],
            key=lambda x: x['age_months']
        )
        # Select the latest one the child is eligible for
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
    """Searches loaded outbreak data by state or district and formats findings."""
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
    response_lines = [f"Recent health alerts for **{location_input.title()}**:"]
    for report in results:
        summary = (
            f"• **{report.get('disease', 'N/A')}** in {report.get('district', 'N/A')}: "
            f"{report.get('cases', 0)} cases, {report.get('deaths', 0)} deaths. "
            f"Status: *{report.get('status', 'N/A')}*."
        )
        response_lines.append(summary)
    response_lines.append("\n**Source:** Integrated Disease Surveillance Programme (IDSP). Please consult official MoHFW channels for the latest information.")
    return "\n".join(response_lines)

# ============================================================================
# ALL YOUR EXISTING ACTIONS, WITH ONE MODIFICATION
# ============================================================================

def run_kb_pipeline(dispatcher: CollectingDispatcher, tracker: Tracker) -> bool:
    """A reusable function to run the full Knowledge Base pipeline."""
    # (This function is correct and requires no changes)
    user_input = tracker.latest_message.get('text')
    glossary_result = health_glossary_handler.lookup(user_input)
    if glossary_result:
        term, definition_dict = glossary_result
        definition = definition_dict.get('def_en', 'No definition found.')
        dispatcher.utter_message(template="utter_found_in_glossary", term=term.upper(), definition=definition)
        return True
    kb_result = semantic_kb_handler.search(user_input)
    if kb_result:
        answer = kb_result.get('answer_en', "I found information but couldn't format it.")
        dispatcher.utter_message(template="utter_found_in_kb", answer=answer)
        return True
    return False

class ActionDefaultFallbackOrchestrator(Action):
    # (This action is correct and requires no changes)
    def name(self) -> Text: return "action_default_fallback_orchestrator"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # ... (logic remains the same)
        corpus_result = search_corpus(tracker.latest_message.get('text'))
        if corpus_result:
            dispatcher.utter_message(text=corpus_result)
            return []
        if run_kb_pipeline(dispatcher, tracker):
            return []
        dispatcher.utter_message(template="utter_fallback")
        return []

class ValidateVaccinationForm(FormValidationAction):
    """Validation logic for the vaccination_form."""
    # (This class is correct and requires no changes)
    def name(self) -> Text: return "validate_vaccination_form"
    async def validate_age(self, slot_value: Any, d: CollectingDispatcher, t: Tracker, dom: DomainDict) -> Dict[Text, Any]:
        return {"age": slot_value} if slot_value else {"age": None}
    async def validate_location(self, slot_value: Any, d: CollectingDispatcher, t: Tracker, dom: DomainDict) -> Dict[Text, Any]:
        return {"location": slot_value} if slot_value else {"location": None}

# -----------------------------------------------------------------------------
# MODIFIED VACCINATION ACTION
# -----------------------------------------------------------------------------
class ActionAskVaccinationSchedule(Action):
    def name(self) -> Text:
        return "action_ask_vaccination_schedule"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # --- CRITICAL BUG FIX FOR PREGNANCY ---
        # We check for the new, specific intent first. This is the "fast lane".
        if tracker.get_intent_of_latest_message() == "ask_vaccination_schedule_pregnant":
            schedule_string = get_schedule_from_json("pregnant")
            if schedule_string:
                dispatcher.utter_message(text=schedule_string)
            else: # Safety net if the JSON fails for some reason
                dispatcher.utter_message(text="I can provide vaccine info for pregnant women, but couldn't retrieve it now. Please consult your doctor.")
            return [] # End the conversation here.
        
        # --- If it's not the special pregnancy intent, proceed with the original form logic ---
        age = tracker.get_slot("age")
        location = tracker.get_slot("location")

        age_text = age if age else "the person"
        if age and ("year" in age.lower() or "month" in age.lower()) and "old" not in age.lower():
            age_text = f"{age} old"

        api_works = False # Your master switch
        if api_works:
            dispatcher.utter_message(template="utter_vaccination_schedule_api", age=age_text, location=location)
        else:
            schedule_string = get_schedule_from_json(age)
            if schedule_string:
                dispatcher.utter_message(text=schedule_string)
            else:
                dispatcher.utter_message(template="utter_vaccination_schedule_fallback", age=age_text, location=location)
            
        return [SlotSet("age", None), SlotSet("location", None)]

# --- ALL OTHER ACTIONS ARE UNCHANGED AND CORRECT ---
class ActionHandleDiseaseQuery(Action):
    def name(self) -> Text: return "action_handle_disease_query"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # (This logic is correct and requires no changes)
        disease = next(tracker.get_latest_entity_values("disease"), None)
        latest_intent = tracker.get_intent_of_latest_message()
        if disease:
            disease_key = disease.lower().replace(" ", "_").replace("-", "_")
            template_map = {"ask_disease_info": f"utter_disease_info_{disease_key}", "ask_symptoms": f"utter_symptoms_{disease_key}", "ask_prevention": f"utter_prevention_{disease_key}"}
            template_name = template_map.get(latest_intent)
            if template_name and template_name in domain.get("responses", {}):
                dispatcher.utter_message(template=template_name)
                return []
        corpus_result = search_corpus(tracker.latest_message.get('text'))
        if corpus_result:
            dispatcher.utter_message(text=corpus_result)
            return[]
        if not run_kb_pipeline(dispatcher, tracker):
            dispatcher.utter_message(template="utter_disease_guidelines_fallback")
        return []

class ActionAskEmergencyContacts(Action):
    """
    This is the definitive, unified logic for this action. It is triggered
    by both 'ask_emergency_contacts' and 'provide_pincode' intents and
    correctly distinguishes between a direct geo-lookup and an emergency request.
    """
    def name(self) -> Text:
        return "action_ask_emergency_contacts"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pincode = tracker.get_slot("pincode") or next(tracker.get_latest_entity_values("pincode"), None)
        user_input_text = tracker.latest_message.get('text', '').strip()
        intent_name = tracker.latest_message['intent'].get('name')

        # SCENARIO A: Geo-Info Lookup. User ONLY provided a pincode.
        # This logic is perfect and remains unchanged.
        if intent_name == "provide_pincode" and re.fullmatch(r'\d{6}', user_input_text):
            contacts = geo_fallback_handler.get_contacts(user_input_text)
            if contacts:
                dispatcher.utter_message(
                    template="utter_geofallback_contact_info",
                    contact_en=contacts.get('contact_en', 'N/A'),
                    contact_odia=contacts.get('contact_odia', 'N/A')
                )
            else:
                dispatcher.utter_message(template="utter_pincode_not_found", pincode=user_input_text)
            return [SlotSet("pincode", None)]

        # SCENARIO B: Emergency Services Lookup.
        # User asked for help AND we have a pincode.
        if pincode:
            api_works = False # Your master switch for the real API

            # THE FIX IS HERE: The `else` block now correctly calls the emergency fallback.
            if api_works:
                dispatcher.utter_message(template="utter_emergency_contacts_api", pincode=pincode)
            else:
                # THIS IS THE CORRECT FALLBACK FOR AN EMERGENCY REQUEST
                dispatcher.utter_message(template="utter_emergency_contacts_fallback", pincode=pincode)
                
            return [SlotSet("pincode", None)]

        # SCENARIO C: Emergency Services request, but no pincode is known. We must ask.
        dispatcher.utter_message(template="utter_ask_pincode")
        return []

class ActionAskOutbreakAlerts(Action):
    """
    This is the definitive and correct action for outbreak alerts. It handles
    the multi-turn conversation with a simple, robust, stateless logic.
    """
    def name(self) -> Text: 
        return "action_ask_outbreak_alerts"
        
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # This stateless logic correctly gets the location from the LATEST user message
        location = next(tracker.get_latest_entity_values("location"), None)
        
        # If the user's *current* message doesn't contain a location, ask for it.
        if not location:
            dispatcher.utter_message(template="utter_ask_location_outbreak")
            return [] # The action ends, waiting for the user to provide the location.
        
        # If a location IS in the current message, proceed directly to the final logic.
        api_works = False # The master switch
        if api_works:
            dispatcher.utter_message(template="utter_outbreak_alerts_api", location=location)
        else:
            outbreak_string = get_outbreaks_from_json(location)
            # The helper function itself will return the "no data" message if needed
            dispatcher.utter_message(text=outbreak_string)

        return [] # This stateless action is now complete.


class ActionMedicineLookup(Action):
    def name(self) -> Text: return "action_medicine_lookup"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # (This logic is correct and requires no changes)
        intent_name = tracker.latest_message['intent'].get('name')
        try:
            if intent_name == "ask_medicine_info":
                medicine_name = next(tracker.get_latest_entity_values("medicine"), None)
                if not medicine_name:
                    dispatcher.utter_message(template="utter_ask_for_medicine")
                    return []
                response = requests.get(f"{MEDICINE_API_URL}/info", params={"name": medicine_name})
                response.raise_for_status()
                dispatcher.utter_message(text=response.json()["summary"])
            elif intent_name == "compare_medicines":
                entities = list(tracker.get_latest_entity_values("medicine"))
                if len(entities) < 2:
                    dispatcher.utter_message(text="To compare, please provide two medicine names, like 'Pan-D vs Pan-40'.")
                    return []
                response = requests.get(f"{MEDICINE_API_URL}/compare", params={"med1": entities[0], "med2": entities[1]})
                response.raise_for_status()
                dispatcher.utter_message(text=response.json()["summary"])
        except requests.exceptions.RequestException as e:
            logging.error(f"Could not connect to the Medicine API: {e}")
            dispatcher.utter_message(template="utter_api_down_medicine")
        return []