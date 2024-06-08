from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from Crypto.Random import get_random_bytes
import base64
import base64
import os

class HelperFunctions:
    
    def generateIV(self):
        iv = get_random_bytes(16)
        return base64.b64encode(iv).decode('utf-8')

    def generate_key_pair(self):

        private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
        )
        
        public_key = private_key.public_key()

        private_key_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_key_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return private_key_pem.decode(), public_key_pem.decode()

    def generate_keys_iv(self):
        key = os.urandom(32)  # 256-bit key for AES-256
        iv = os.urandom(16)   # 128-bit IV for AES
        return {"key": base64.b64encode(key).decode('utf-8'), "iv": base64.b64encode(iv).decode('utf-8')}


