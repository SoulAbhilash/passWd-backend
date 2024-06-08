from Crypto.Random import get_random_bytes
import base64
import os

b = get_random_bytes(16)
a = base64.b64encode(b).decode('utf-8')

key = os.urandom(32)  # 256-bit key for AES-256
iv = os.urandom(16)   # 128-bit IV for AES
print(base64.b64encode(key).decode('utf-8'), base64.b64encode(iv).decode('utf-8'))