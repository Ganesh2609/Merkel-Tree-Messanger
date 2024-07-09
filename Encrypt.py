from cryptography.fernet import Fernet

def encryption(value):
    with open('key.txt','r') as f:
        mykey = f.read().encode()
        
    #print(key)
        
    key = Fernet(mykey)
    encrypted = key.encrypt(value)
    return encrypted

def decryption(value):
    with open('key.txt','r') as f:
        mykey = f.read().encode()
       
    key = Fernet(mykey)
    decrypted = key.decrypt(value)
    return decrypted
