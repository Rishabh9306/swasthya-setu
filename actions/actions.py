from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionAskVaccinationSchedule(Action):
    def name(self) -> Text:
        # CORRECTED NAME to match domain.yml and rules.yml
        return "action_ask_vaccination_schedule"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        age = tracker.get_slot("age")
        location = tracker.get_slot("location")

        if not age:
            dispatcher.utter_message(template="utter_ask_age")
            return []
        if not location:
            dispatcher.utter_message(template="utter_ask_location")
            return []

        api_works = True
        if api_works:
            dispatcher.utter_message(template="utter_vaccination_schedule_api", age=age, location=location)
        else:
            dispatcher.utter_message(template="utter_vaccination_schedule_fallback", age=age, location=location)
        return [SlotSet("age", None), SlotSet("location", None)]


class ActionAskOutbreakAlerts(Action):
    def name(self) -> Text:
        # CORRECTED NAME
        return "action_ask_outbreak_alerts"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("location")
        if not location:
            dispatcher.utter_message(template="utter_ask_location_outbreak")
            return []
        api_works = True
        if api_works:
            dispatcher.utter_message(template="utter_outbreak_alerts_api", location=location)
        else:
            dispatcher.utter_message(template="utter_outbreak_alerts_fallback", location=location)
        return [SlotSet("location", None)]


class ActionAskEmergencyContacts(Action):
    def name(self) -> Text:
        # CORRECTED NAME
        return "action_ask_emergency_contacts"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pincode = tracker.get_slot("pincode")
        if not pincode:
            dispatcher.utter_message(template="utter_ask_pincode")
            return []
        api_works = True
        if api_works:
            dispatcher.utter_message(template="utter_emergency_contacts_api", pincode=pincode)
        else:
            dispatcher.utter_message(template="utter_emergency_contacts_fallback", pincode=pincode)
        return [SlotSet("pincode", None)]


class ActionHandleDiseaseQuery(Action):
    # This action was already correctly named and working. No changes needed here.
    def name(self) -> Text:
        return "action_handle_disease_query"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        disease = next(tracker.get_latest_entity_values("disease"), None)
        latest_intent = tracker.get_intent_of_latest_message()
        if not disease:
            dispatcher.utter_message(template="utter_disease_guidelines_fallback")
            return []
        disease_key = disease.lower().replace(" ", "_")
        template_map = {
            "ask_disease_info": f"utter_disease_info_{disease_key}",
            "ask_symptoms": f"utter_symptoms_{disease_key}",
            "ask_prevention": f"utter_prevention_{disease_key}",
        }
        template_name = template_map.get(latest_intent)
        if template_name and template_name in domain.get("responses", {}):
             dispatcher.utter_message(template=template_name)
        else:
             dispatcher.utter_message(template="utter_disease_guidelines_fallback")
        return []