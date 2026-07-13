# M     M M     M  GGGGGGGGG  EEEEEEEE    RRRR
# MM   MM MM   MM  G          E           R   R
# M M M M M M M M  G    GGGG  EEEEEEEE    RRRR
# M  M  M M  M  M  G       G  E           R   R
# M     M M     M  GGGGGGGGG  EEEEEEEE    R    R



import socket, os, time, sys
import base64
import json


encoded_text = None
decoded_text = None



def encodef(text):
    utf_encode = text.encode('utf-8')
    global encoded_text
    encoded_text = base64.b64encode(utf_encode)
def decodef(bs64bytes):
    rslt = base64.b64decode(bs64bytes)
    global decoded_text
    decoded_text = rslt.decode('utf-8')
    

version = "v2.5.0-release"

timen = None

# FUNCS


def get_time():
    global timen
    timen = time.asctime()




def connect_client(ipf, portf):
    try:
        client.connect((ipf, portf))
    except Exception as e:
        print("Error while connecting! Retrying...")
        connect_client(ipf, portf)




def clear():
    os.system("cls")




clear()

get_time()
print(f"Welcome to MMger(Messenger Manager) {version}")

print("1. Connect \n2. Create server\n")

cmd = input(f"MESSENGER-MANAGER> ")


try:
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
except FileNotFoundError:
    print("config.json was not found or was deleted, please recover it")
    print("config file example: ")
    print("name: config.json")
    print('configs: {\n    "upload_config": true,\n    "ip": "localhost",\n    "port": 25565,\n    "password": 1234\n}')
    input("Click enter to leave...")
    exit()
try:
    config_turned_on = config["upload_config"]
    imported_ip = config["ip"]
    imported_port = config["port"]
    imported_pass = config["password"]
except Exception as e:
    print("config.json was erassed or one of configurations was not found(or changed), please check and recover it")
    print("config file example: ")
    print("name: config.json")
    print('configs: {\n    "upload_config": true,\n    "ip": "localhost",\n    "port": 25565,\n    "password": 1234\n}')
    input("Click enter to leave...")
    exit()




#  CCCCC  L         III   EEEEEEE    N     N     TTTTTTTT
# C       L          I    E          N N   N        TT
# C       L          I    EEEEEEE    N  N  N        TT
# C       L          I    E          N   N N        TT
#  CCCCC  LLLLLLL   III   EEEEEEE    N    NN        TT








if cmd == "1":
    client = socket.socket()

    clear()
    port = None
    if config_turned_on == True:
        print("")
        ip = imported_ip
        port = imported_port
        connect_client(ip, port)
        does_have_pswd = client.recv(1024).decode('utf-8')
    else:
        print("Please, enter IP and port")
        ip = input("IP> ")
        clear()
        if ip == "localhost":
            port = 25565
        else:
            port = int(input("PORT> "))
            connect_client(ip, port)
            does_have_pswd = client.recv(1024).decode('utf-8')
    
    
    
    
    attempts = 3
    def pasw():
        global attempts
        if config_turned_on == True:
            password_c = imported_pass
            client.send(password_c.encode('utf-8'))
            crslt = client.recv(1024).decode('utf-8')
            if crslt == "wrg":
                pasw()
                attempts -= 3
                if attempts == 0:
                    client.close()
                    print("Wrong password!")
                    input("Click enter to leave...")
                    exit()
                elif crslt == "scs":
                    print("Correct password")
        else:
            password_c = input("PASSWORD> ")
            client.send(password_c.encode('utf-8'))
            crslt = client.recv(1024).decode('utf-8')
            if crslt == "wrg":
                attempts -= 1
                pasw()
                if attempts == 0:
                    client.close()
                    print("Wrong password! No attempts!")
                    input("Click enter to leave...")
                    exit()
                elif crslt == "scs":
                    print("Correct password!")




    if does_have_pswd == "clt.psw.y":
        pasw()




    connection = True



    while connection:
        
        print(f"The {ip}:{port} is typing...\n\n")
        msg = client.recv(1024)
        decodef(msg)
        if decoded_text == "server.chat.clear":
            clear()
        get_time()
        print(f"\n{ip}:{port}> {decoded_text} [{timen}]\n")


        sendorc = input("> ")
        encodef(sendorc)
        get_time()
        print(f"(SENDING...) CLIENT: {sendorc} [{timen}]\n")
        client.send(encoded_text)
        print(f"\r(SENDED) CLIENT: {sendorc} [{timen}]")
        
    client.close()







#  SSSSSSS   EEEEEEEEEE  RRRRR      V       V  EEEEEEEEEE    RRRRR
# S          E           R     R     V     V   E             R     R
#  SSSSSSS   EEEEEEEEEE  RRRRRR       V   V    EEEEEEEEEE    RRRRRR
#         S  E           R      R      V V     E             R     R
#  SSSSSSS   EEEEEEEEEE  R       R      V      EEEEEEEEEE    R      R






elif cmd == "2":
    server = socket.socket()
    print("Importing from config...")
    if config_turned_on == True:
        ips = imported_ip
        ports = imported_port
            
            
        password = imported_pass
    else:
            
            
        ports = None
        print("Please, enter IP and port")
        ips = input("IP> ")
        if ips == "localhost":
                
            ports = 25565
                
        else:
                
            ports = int(input("PORT> "))
            
            
        password = input("PASSWORD(just click enter you want without password)> ")
    clear()


    try:
        
        server.bind((ips, ports))
        print("Waiting for connection...")
        server.listen()
        client, address = server.accept()
        text = f"Connected! IP: {address}"
        
        if password == " ":
            
            password = None
        if password == "":
            
            password = None
            
        if password != None:
            
            client.send("clt.psw.y".encode('utf-8'))
            text = f"Connected! IP:{address}, Waiting when the other side will send the correct password..."
            cpassword = client.recv(1024).decode('utf-8')
            
            if cpassword != password:
                
                client.send("wrg".encode('utf-8'))
                cpassword = client.recv(1024).decode('utf-8')
                
                if cpassword != password:
                    
                    client.send("wrg".encode('utf-8'))
                    cpassword = client.recv(1024).decode('utf-8')
                    
                    if cpassword != password:


                        client.close()
                        server.close()
                        exit()
                        
                    else:
                        client.send("scs".encode('utf-8'))
                else:
                    client.send("scs".encode('utf-8'))
            else:
                client.send("scs".encode('utf-8'))
        else:
            client.send("clt.psw.n".encode('utf.8'))
            
        print(text)

    except Exception as e:
        print(f"Error! error code: {e}")
    server_c = True




    while server_c:
        sendors = input("> ")
        if sendors == "server.chat.clear":
            clear()
        if sendors == "server.disconnect":
            server.close()
            client.close()
            server_c = False
        get_time()
        print(f"(SENDING...) {ips}:{ports}> {sendors} [{timen}]\n")
        encodef(sendors)
        try:
            client.send(encoded_text)
        except Exception as e:
            print("Error! Client was disconnected!")
            input("Click enter to leave...")

        print(f"(SENDED) {ips}:{ports}> {sendors} [{timen}]")
        msg = client.recv(1024)
        decodef(msg)
        get_time()
        print(f"{address}: {decoded_text} [{timen}]")
    server.close()
    client.close()


else:
    print("Wrong input! Please enter 1 or 2!\n\n\n\n\n\n")
    input("Click enter to leave...")

    
