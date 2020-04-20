# Restaurant-Search-Chatbot

# Business Statement:

Build a domain-specific chatbot, specifically, a restaurant search chatbot. The bot will be able to 'talk' to users in English, and will help them search for restaurants offering multiple cuisines, suiting different budgets, etc., in several cities. You will be using an open-source machine learning (ML) framework called Rasa for building these conversational bots.
This module contains two sessions. In the first session, you will learn how to build a chatbot and deploy it on a public channel such as Slack, Facebook, etc. The second session defines the problem statement, deliverables, etc., of the group project.
 
 ‘Building Chatbots with Rasa’ 
 
rasa - 1.7.0      
rasa-sdk - 1.7.0 
python 3.7

- Rasa setup
run rasa init --no-prompt

- Rasa nlu layer
Trained the NlU with nlu.md with samples
run rasa data convert nlu --data data/nlu.md --out data/data.json -f json in terminal to convert nlu.md to data.json
run rasa-nlu-trainer : It opens browser on http://localhost:62092/
add examples for bot to understand the entities, intent 
run rasa train nlu 
run rasa shell nlu to check the confidence

- Rasa core layer
create some stories in stories.md
run rasa interactive : train the stories
run rasa train (nlu and core gets trained)

- run rasa run actions : to make the action server up 
- run rasa shell to test the bot

- smtplib for email functions
