import socket as skt

IP = "127.0.0.1"
PORT = 5050

flag = "y"
 
with skt.socket(skt.AF_INET, skt.SOCK_STREAM) as client :
    client.connect((IP, PORT))
    
    while flag != "n" :
        client.sendall(input("Inserisci un qualcosa da trasformare...\n").encode())
        data = client.recv(1024)
        
        print("Reply: ", data.decode())
        
        flag = input("continue ? y/n")
        if flag == "n":
            client.sendall("password".encode())