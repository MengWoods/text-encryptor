from cryptography.fernet import Fernet

class fernet:
    def __init__(self, key):
        self.key = key
        # Initialize the cipher
        self.cipher_suite = Fernet(key)

    def generateKey(self):
        self,key =  Fernet.generate_key()

    def encrypt(self, text):
        self.byte_text = bytes(text, "utf-8")
        self.cipher_text = self.cipher_suite.encrypt(self.byte_text)
        return self.cipher_text
    
    def decrypt(self, encrypted_text):
        self.decrypted_text = self.cipher_suite.decrypt(encrypted_text).decode()
        return self.decrypted_text
    
