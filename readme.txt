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
