# Chatbot-using-PyTorch

A Chatbot which connects server and client using TCP connection (Socket Programming).

## To execute the project

1. Activate a conda environment (ChatBot)

2. Install and import the following packages :
* pip install torch
* pip install numpy
* pip install nltk
* pip install nlp
		
3. If any changes are made to the 'pattern' and 'responses' in the intents.json dataset. Then execute the train.py file to train the model (change the hyperparameters according to the need).

4. To execute the chatbot, 
* first execute the nltk_utils.py
* then model.py
* followed by train.py
* and finally open the server (server.py) and then client (client.py) to establish connection between server and client using TCP connection.

### Enjoy....
