import socket as sk
import threading as td
import time
import pickle as pc
import Encrypt

host = "192.168.176.164"     
port = 41720

server = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
server.bind((host,port))
    
server.listen()
clients = []
aliases = []  
address = []
count = 0
    
def connect_client(client, adr):
    global count
    client.send(Encrypt.encryption(pc.dumps(("Enter your name : ",))))
    alias = Encrypt.decryption(client.recv(1024)).decode()              
    aliases.append(alias)
    clients.append(client)
    address.append(adr)
    print("[SERVER] ",alias," ",adr," has connected to the server [",time.strftime("%H:%M",time.localtime()),"]",sep="")
    count+=1
    print("Active Connections :",count,end="\n\n")
    handle(client)
            
def handle(client):
    global count
    while True:
        try :
            got_from_client = client.recv(102400)  
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            print("[SERVER] ",alias," ",address[index]," has disconnected from the server [",time.strftime("%H:%M",time.localtime()),"]",sep="")
            count-=1
            print("Active Connections :",count,end="\n\n")
            aliases.pop(index)
            address.pop(index)
            break
        got_from_client = pc.loads(Encrypt.decryption(got_from_client))
        rec = got_from_client[3]
        sender = aliases[clients.index(client)]
        reciever = ""   
        try:
            reciever = clients[aliases.index(rec)]
        except:
            print("[SERVER] ERROR : The reciever of the message was not found")
            print("                ",sender," please recheck your recipient...\n")     
            continue
        to_be_sent = (got_from_client[0],got_from_client[1],got_from_client[2],sender, got_from_client[4])
        to_be_sent = Encrypt.encryption(pc.dumps(to_be_sent))
        reciever.send(to_be_sent)                          

def Server():
    global count
    print("The server is running...\n")
    while True:
        client, adr = server.accept()
        thread = td.Thread(target=connect_client, args=(client,adr))
        thread.start()
        
if __name__ == "__main__":
    Server()