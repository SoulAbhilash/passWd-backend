from Crypto.Random import get_random_bytes
import base64

b = get_random_bytes(16)
a = base64.b64encode(b).decode('utf-8')
print(a)