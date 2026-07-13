# M     M M     M  GGGGGGGGG  EEEEEEEE    RRRR
# MM   MM MM   MM  G          E           R   R
# M M M M M M M M  G    GGGG  EEEEEEEE    RRRR
# M  M  M M  M  M  G       G  E           R   R
# M     M M     M  GGGGGGGGG  EEEEEEEE    R    R



import socket, os, time, sys
import base64


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
    

version = "v1.0.1-release"

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
        connect_client(ipf, port)




def clear():
    os.system("cls")




clear()

get_time()
print(f"Welcome to MMger(Messenger Manager) {version}")

print("1. Connect \n2. Create server\n")

cmd = input(f"MESSENGER-MANAGER> ")






#  CCCCC  L         III   EEEEEEE    N     N     TTTTTTTT
# C       L          I    E          N N   N        TT
# C       L          I    EEEEEEE    N  N  N        TT
# C       L          I    E          N   N N        TT
#  CCCCC  LLLLLLL   III   EEEEEEE    N    NN        TT








if cmd == "1":
    client = socket.socket()

    clear()
    port = None
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
        password_c = input("PASSWORD> ")
        client.send(password_c.encode('utf-8'))
        crslt = client.recv(1024).decode('utf-8')
        if crslt == "wrg":
            pasw()
            attempts -= 1
            if attempts == 0:
                client.close()
                exit()
        elif crslt == "scs":
            print("success!")




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

    
