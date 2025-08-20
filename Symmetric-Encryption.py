from cryptography.fernet import Fernet

#Generate a secret key
key = Fernet.generate_key()
cipher = Fernet(key)

#print("Secret Key (keep confidential):", key.decode())

message = "i creat the code to encrypte the code for babi energie project.".encode()
# encode() transfer text to bytes

encrypted_message = cipher.encrypt(message)
print("\nEncrypted Message:", encrypted_message.decode())

decrypted_message = cipher.decrypt(encrypted_message)
print("\nDecrypted Message:", decrypted_message.decode())
