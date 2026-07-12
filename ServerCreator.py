# server
import socket, os



os.system("cls")


server = socket.socket()
print("please, enter IP\n")
ip = input("IP> ")
port = int(input("PORT> "))
server.bind((ip, port))

server.listen()

client, address = server.accept()
os.system('cls')

connection = True

while connection:
    client.send(input("Я: \n").encode('utf-8'))
    print("Other user is typing...\n")
    msg = client.recv(1024).decode('utf-8')
    print(msg)
    print("")
    if msg == "leave.server":
        server.close
        client.close
        connection = False


input("Click the enter to leave...")