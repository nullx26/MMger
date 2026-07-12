# client
import socket, os

client = socket.socket()

print("Please, enter IP\n")

ip = input("IP> ")
port = int(input("PORT> "))

client.connect((ip, port))

os.system("cls")

connection = True

while connection:
    print("Other user is typing...\n")
    msg = client.recv(1024).decode('utf-8')
    print(msg)
    print("")
    if msg == "leave.server":
        client.close
        connection = False

    client.send(input("Я:\n").encode('utf-8'))

input("Click the enter to leave...")