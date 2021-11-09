# Chatbot-using-PyTorch

A Rule based chatbot which makes use of Feed Forward Neural Network (FNN) to train the dataset and let the bot respond to the user messages. It can be used in any context (after properly using the dataset for the given context to train the model).

The following tools/libraries has been used:
- PyTorch (to call the Neural Network and train the model)
- NLTK (for tokenizing, stemming and bag of words)
- Socket Programming
- pip install gTTS (Google Text to Speech API)
- pip install playsound  
- pip install pyttsx3  (To convert text files into speech)

## Theory behind the Project

### 1. Creating the Dataset (intents.json)

![image](https://user-images.githubusercontent.com/48097039/140949740-ae23edd8-0d96-4451-ae07-97d95c7fe0c6.png)

You can customize it according to your own use case. Just define a new tag, possible patterns, and possible responses for the chat bot. You have to re-run the training whenever this file is modified.

### 2. NLP Basics for training of Data

**Tokenization** - take the sentence and each of the words in put in a array of words.

**Stemming** - to get the root word.

**Bag of words**

![image](https://user-images.githubusercontent.com/48097039/140950153-e47756d7-ebb3-4bad-843f-53dd96db6dbf.png)

### 3. Implementing the Neural Network

we are using a Feed Forward Neural Network (FNN) with 1 hidden layer.

### 4. Implement the chat

The chatbot is implemented using Socket Programming.

### 5. Text to Speech

The response from the bot is then converted to speech using Google API mentioned above.


## Key points (to refresh memory)

The **activation function** is a non-linear transformation that we do over the input before sending it to the next layer of neurons or finalizing it as output.

we are using **ReLu activation** function (outputs the input itself if it is positive... else 0).
(The main advantage of using the ReLU function over other activation functions is that it does not activate all the neurons at the same time. What does this mean ? If you look at the ReLU function if the input is negative it will convert it to zero and the neuron does not get activated.)

refer https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9 for understanding _epoch, batch size and iteration._


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
