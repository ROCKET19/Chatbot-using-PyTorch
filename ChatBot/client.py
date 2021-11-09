import socket

import pyttsx3
# initialize Text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 180)


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("\nHi I am J.A.R.V.I.S. wLet's chat!!! type 'bei' to exit\n")
    while True:
        sentence = input("You: ")
        if sentence == 'bei':
            break
        else:
            s.sendall(str.encode(sentence))

        data = s.recv(1024).decode()

        print(data)

        engine.say(data[8:-1])
        engine.runAndWait()

    # data = s.recv(1024)


    # exec(open('chat.py').read())

# print('Received', repr(data))

print("\nConnection Closed Successfully...")