from cryptography.fernet import Fernet

key = Fernet.generate_key()
#print(key)
with open("key.txt", 'w') as f:
    f.write(key.decode())
    
