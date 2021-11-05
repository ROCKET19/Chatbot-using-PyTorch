import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        sentence = input("You: ")
        if sentence == 'bei':
            break
        else:
            s.sendall(str.encode(sentence))

        data = s.recv(1024).decode()

    # data = s.recv(1024)
        print(data)

    # exec(open('chat.py').read())

# print('Received', repr(data))

print("\nConnection Closed Successfully...")