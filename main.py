from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
print("Key:", key)

# Initialize the cipher
cipher_suite = Fernet(key)

# Text to be encrypted
msg = input("Please enter some text: ")
message = bytes(msg, "utf-8")

# Encrypt the text
cipher_text = cipher_suite.encrypt(message)

# Print the encrypted text and key

print("Encrypted data:", cipher_text)

decrypted_message = cipher_suite.decrypt(cipher_text).decode()

print("Decrypted data:", decrypted_message)