# actions/actions.py (Definitive Version)

from typing import Any, Text, Dict, List
import re
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

from knowledge_base.fallback_system import GeoFallback, SemanticKB, HealthGlossary
from knowledge_base.vector_store import load_vector_store, search_corpus

# --- INITIALIZE KNOWLEDGE BASES (No changes needed) ---
geo_fallback_handler = GeoFallback()
semantic_kb_handler = SemanticKB()
health_glossary_handler = HealthGlossary()
load_vector_store()

def run_kb_pipeline(dispatcher: CollectingDispatcher, tracker: Tracker) -> bool:
    """A reusable function to run the full Knowledge Base pipeline."""
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

# --- LOW-CONFIDENCE ORCHESTRATOR (Correct & Stable) ---
class ActionDefaultFallbackOrchestrator(Action):
    def name(self) -> Text:
        return "action_default_fallback_orchestrator"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message.get('text')

        # --- FALLBACK CHAIN STEP 1: RAG Corpus Search ---
        corpus_result = search_corpus(user_input)
        if corpus_result:
            dispatcher.utter_message(text=corpus_result)
            return []
        # --- FALLBACK CHAIN STEP 2: KB Search ---
        if run_kb_pipeline(dispatcher, tracker):
            return []
        # --- FALLBACK CHAIN STEP 3: Final Safety Net ---
        dispatcher.utter_message(template="utter_fallback")
        return []

# --- SMART ACTIONS WITH FINAL BUG FIXES ---

class ValidateVaccinationForm(FormValidationAction):
    """Validation logic for the vaccination_form."""
    def name(self) -> Text:
        return "validate_vaccination_form"

    async def validate_age(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        if slot_value:
            return {"age": slot_value}
        return {"age": None}

    async def validate_location(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        if slot_value:
            return {"location": slot_value}
        return {"location": None}

class ActionAskVaccinationSchedule(Action):
    """SUBMIT action for the form with the final grammar fix."""
    def name(self) -> Text:
        return "action_ask_vaccination_schedule"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        age = tracker.get_slot("age")
        location = tracker.get_slot("location")

        age_text = age
        if ("year" in age.lower() or "month" in age.lower()) and "old" not in age.lower():
            age_text = f"{age} old"

        api_works = False
        if api_works:
            dispatcher.utter_message(template="utter_vaccination_schedule_api", age=age_text, location=location)
        else:
            dispatcher.utter_message(template="utter_vaccination_schedule_fallback", age=age_text, location=location)
            
        return [SlotSet("age", None), SlotSet("location", None)]

class ActionHandleDiseaseQuery(Action):
    """Smart action with KB pivot, no changes needed."""
    def name(self) -> Text:
        return "action_handle_disease_query"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        disease = next(tracker.get_latest_entity_values("disease"), None)
        latest_intent = tracker.get_intent_of_latest_message()

        # Plan A: Happy path (NLU found a specific disease entity).
        if disease:
            disease_key = disease.lower().replace(" ", "_").replace("-", "_")
            template_map = {"ask_disease_info": f"utter_disease_info_{disease_key}", "ask_symptoms": f"utter_symptoms_{disease_key}", "ask_prevention": f"utter_prevention_{disease_key}"}
            template_name = template_map.get(latest_intent)
            
            if template_name and template_name in domain.get("responses", {}):
                dispatcher.utter_message(template=template_name)
                return []

        # Plan B: NLU was wrong, missed the entity, or there's no template.
        # Pivot to the FULL fallback chain, starting with the RAG corpus.
        corpus_result = search_corpus(tracker.latest_message.get('text'))
        if corpus_result:
            dispatcher.utter_message(text=corpus_result)
            return[]

        if not run_kb_pipeline(dispatcher, tracker):
            # Only if all systems fail, give the generic guidelines message.
            dispatcher.utter_message(template="utter_disease_guidelines_fallback")
        return []

class ActionAskEmergencyContacts(Action):
    """
    FINAL UNIFIED LOGIC: This action now correctly distinguishes between
    a standalone pincode query and an emergency contact query.
    """
    def name(self) -> Text:
        return "action_ask_emergency_contacts"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pincode = tracker.get_slot("pincode")
        user_input_text = tracker.latest_message.get('text', '').strip()

        # If a pincode was extracted, we decide what to do with it.
        if pincode:
            # SCENARIO A: User typed ONLY a pincode.
            # This is a GEOGRAPHICAL lookup.
            if user_input_text == pincode:
                contacts = geo_fallback_handler.get_contacts(pincode)
                if contacts:
                    dispatcher.utter_message(
                        template="utter_geofallback_contact_info",
                        contact_en=contacts.get('contact_en', 'N/A'),
                        contact_odia=contacts.get('contact_odia', 'N/A')
                    )
                else:
                    dispatcher.utter_message(template="utter_pincode_not_found", pincode=pincode)
                return [SlotSet("pincode", None)]

            # SCENARIO B: User provided pincode in a sentence (e.g., "my pincode is...")
            # or after being prompted. This is an EMERGENCY CONTACTS request.
            else:
                api_works = True  # Set to True to test API path
                template = "utter_emergency_contacts_api" if api_works else "utter_emergency_contacts_fallback"
                dispatcher.utter_message(template=template, pincode=pincode)
                return [SlotSet("pincode", None)]

        # SCENARIO C: No pincode was provided in the utterance. We must ask.
        else:
            dispatcher.utter_message(template="utter_ask_pincode")
            return []

class ActionAskOutbreakAlerts(Action):
    """This action's logic is stable. No changes needed."""
    def name(self) -> Text: return "action_ask_outbreak_alerts"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("location")
        if not location:
            dispatcher.utter_message(template="utter_ask_location_outbreak")
        else:
            dispatcher.utter_message(template="utter_outbreak_alerts_fallback", location=location)
            return [SlotSet("location", None)]
        return []