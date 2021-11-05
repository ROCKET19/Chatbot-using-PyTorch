import socket

import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

bot_name = "Jarvis"

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:        # SOCK_STREAM is the socket type for TCP,
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        while True:
            try:
                data = conn.recv(1024)

                sentence = str(data)
                sentence = sentence[2:-1]
                bla = sentence

                sentence = tokenize(sentence)
                X = bag_of_words(sentence, all_words)
                X = X.reshape(1, X.shape[0])
                X = torch.from_numpy(X)

                output = model(X)

                _, predicted = torch.max(output, dim=1)
                tag = tags[predicted.item()]

                probs = torch.softmax(output, dim=1)
                prob = probs[0][predicted.item()]

                if prob.item() > 0.7:

                    for intent in intents["intents"]:
                        if tag == intent["tag"]:
                            # print(f"{bot_name}: {random.choice(intent['responses'])}")
                            y = bot_name + ": " + random.choice(intent['responses'])
                            # conn.sendall(str.encode(y))
                            conn.send(y.encode())

                else:
                    # print(f"{bot_name}: I don't understand...")
                    # conn.sendall(str.encode("Jarvis: I don't understand"))
                    y = bot_name + ": " + "I don't understand..."
                    conn.send(y.encode())

                if not data:
                    break
                # exec(open('chat.py').read())
                    conn.sendall(str.encode("Connection Closed"))

            except:
                pass
