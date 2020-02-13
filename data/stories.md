## full flow
* greet
  - utter_greet
  - utter_explain_process
  - utter_ask_continent
* inform{"continent": "asia"}
  - utter_ask_activity_type
* inform{"activity_type": "outdoors"}
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
* inform{"continent": "asia"}
  - utter_ask_activity_type
* inform{"activity_type": "outdoors"}
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
* inform{"continent": "asia"}
  - utter_ask_activity_type
* inform{"activity_type": "outdoors"}
  - utter_ask_budget
* ask_recommend
  - action_get_recommendation
  - utter_recommend
  
## 1 question flow
* greet
  - utter_greet
  - utter_explain_process
  - utter_ask_continent
* inform{"continent": "asia"}
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
