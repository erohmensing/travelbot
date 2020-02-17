## full flow
* greet
  - utter_greet
  - utter_explain_process
  - utter_ask_continent
* inform{"continent": "asia"} OR inform
  - utter_ask_activity_type
* inform{"activity_type": "outdoors"} OR inform
  - utter_ask_budget
* affirm OR deny
  - utter_ask_children
* affirm OR deny
  - action_get_recommendation
  - utter_recommend

## 3 question flow
* greet
  - utter_greet
  - utter_explain_process
  - utter_ask_continent
* inform{"continent": "asia"} OR inform
  - utter_ask_activity_type
* inform{"activity_type": "outdoors"} OR inform
  - utter_ask_budget
* affirm OR deny
  - utter_ask_children
* ask_recommend
  - action_get_recommendation
  - utter_recommend

## 2 question flow
* greet
  - utter_greet
  - utter_explain_process
  - utter_ask_continent
* inform{"continent": "asia"} OR inform
  - utter_ask_activity_type
* inform{"activity_type": "outdoors"} OR inform
  - utter_ask_budget
* ask_recommend
  - action_get_recommendation
  - utter_recommend

## 1 question flow
* greet
  - utter_greet
  - utter_explain_process
  - utter_ask_continent
* inform{"continent": "asia"} OR inform
  - utter_ask_activity_type
* ask_recommend
  - action_get_recommendation
  - utter_recommend

## direct recommendation
* greet
  - utter_greet
  - utter_explain_process
  - utter_ask_continent
* ask_recommend
  - action_get_recommendation
  - utter_recommend

## bot challenge
* bot_challenge
  - utter_iamabot

## Story from conversation with aab048cb-7bd9-4460-b99d-56d4b84afac8 on February 14th 2020

* greet
    - utter_greet
    - utter_explain_process
    - utter_ask_continent
* inform{"continent":"asia"}
    - slot{"continent":"asia"}
    - utter_ask_activity_type
* inform
    - utter_ask_budget
    - slot{"continent":"asia"}
    - action_get_recommendation
    - slot{"recommended_location":"Dubai"}
    - slot{"activities_link":"https://www.getyourguide.co.uk/s/?q=Dubai"}
    - utter_recommend
* request_activity_link
    - utter_activity_link
