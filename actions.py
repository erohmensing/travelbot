# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


import json
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionRecommend(Action):
    """Takes in filters of user preferences, pulls relevant activities.

    Pulls the city from the top activity on the list, and returns the city,
    as well as a list of activities for that city.
    """

    def name(self) -> Text:
        return "action_get_recommendation"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        filters = {
            "continent": tracker.get_slot("continent"),
            "activity_type": tracker.get_slot("activity_type"),
            "price": tracker.get_slot("price"),
            "family_friendly": tracker.get_slot("family_friendly"),
        }

        # dispatcher.utter_message(text=f"Here are the filters I received: {json.dumps(filters, indent=2)}")
        # dispatcher.utter_message(text="The following suggestion is mocked, because it's not hitting any APIs.")

        # activities = mock_api.get_activities(filters=filters)
        # city = activities[0].get("city")
        # query_params = "some_string_formatting_filters_and_also_city"
        # activities_link = f"https://www.getyourguide.co.uk/s/?{query_params}"

        # just for now...
        city = "Dubai"
        activities_link = f"https://www.getyourguide.co.uk/s/?q={city}"

        return [SlotSet("recommended_location", city), SlotSet("activities_link", activities_link)]
