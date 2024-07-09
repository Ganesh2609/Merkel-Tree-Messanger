import socket as sk
import threading as td
import pickle as pc
import Encrypt
import sys
import hashlib
import time
import os

host = "192.168.176.164"     
port = 41720
alias = ""
dire = [""]*2   
client = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
client.connect((host,port))

def receive():
    global alias
    while True:
        message = client.recv(102400)
        message = Encrypt.decryption(message)
        data = pc.loads(message)
        if len(data) == 1 :
            alias = input("Enter your name : ")
            alias_to_send = Encrypt.encryption(alias.encode())
            client.send(alias_to_send)
            dire[0] = "Sent/" + alias
            dire[1] = "Recieved/" + alias
            for i in dire:
                if not os.path.exists(i):
                    os.makedirs(i)
        elif len(data) == 5 :
            file_data = data[0]
            file_name = data[2]
            hash_value = data[1]
            sender = data[3]
            block_size = data[4]
            
            print(f"\nReceiving file {file_name} from {sender}")
            
            path = dire[1]+ "/" + file_name
            with open(path, 'wb') as file:
                file.write(file_data)
                file.close()

            print("File has been received successfully")
            
            with open(path, "rb") as f:
                blocks = []
                binary_data_read = f.read(block_size)
                while binary_data_read != b"":
                    blocks.append(binary_data_read)
                    binary_data_read = f.read(block_size)
                f.close()
            
            file_hash = build_merkle_tree(blocks)
            if file_hash == hash_value:
                print("File Authentication is successful") 
            else:
                print("File Authentication has failed")

def send():
    global alias
    while True:
        user = input("Enter the user to send to : ")
        file_name = input("Enter the file name : ")
        path = dire[0] + "/" + file_name
        block_size = int(input("Enter the block size : "))
        with open(path, "rb") as f: 
            binary_data = f.read()
            f.seek(0)
            
            blocks = []
            binary_data_read = f.read(block_size)
            while binary_data_read != b"":
                blocks.append(binary_data_read)
                binary_data_read = f.read(block_size)   
                
            f.close()
            
        hash_root = build_merkle_tree(blocks)
        data = (binary_data, hash_root, file_name, user, block_size)
        out = Encrypt.encryption(pc.dumps(data))
        client.send(out)

def build_merkle_tree(data_blocks):
    if len(data_blocks) == 0:
        raise ValueError("No data blocks to build the Merkle tree.")

    current_level = [hashlib.sha256(block).hexdigest() for block in data_blocks]

    while len(current_level) > 1:
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])

        next_level = [hashlib.sha256((current_level[i] + current_level[i + 1]).encode()).hexdigest() for i in range(0, len(current_level), 2)]

        current_level = next_level

    merkle_root = current_level[0]
    return merkle_root         

receive_thread = td.Thread(target=receive)
receive_thread.start()

time.sleep(1)

send_thread = td.Thread(target=send)
send_thread.start()
