from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


#Generate RSA key
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

#Create cipher objects for encryption and decryption
cipher_encrypt = PKCS1_OAEP.new(public_key)
cipher_decrypt = PKCS1_OAEP.new(private_key)


#b for transfer to bytes
message = b"i creat the code to encrypte the code for babi energie project.(Asymmetric encryption)"
print("Original Message:", message.decode())


#Encrypt the message
encrypted_message = cipher_encrypt.encrypt(message)
print("\nEncrypted Message:", encrypted_message)


#Decrypt the message
decrypted_message = cipher_decrypt.decrypt(encrypted_message)
print("\nDecrypted Message:", decrypted_message.decode())

