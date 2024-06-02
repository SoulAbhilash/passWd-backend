from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
from dotenv import dotenv_values

class CryotoManager:
    """
    Manages encryption and decryption using AES with a private key.
    """

    def __init__(self) -> None:
        """
        Initializes the CryotoManager with a key loaded from a secure `.env` file.
        """

        __env_vars = dotenv_values(".env.secure")
        self.__key:str = str(__env_vars.get("KEY"))  # Store key as a string (unencoded)

        if not self.__key:
            raise ValueError("Missing 'KEY' in .env.secure file")

    def encrypt(self, data: str, iv: str ) -> str:
        """
        Encrypts data using AES with the private key.

        Args:
            data: The data to encrypt (bytes).

        Returns:
            A tuple containing the encrypted data (bytes) and the initialization vector (bytes).
        """
        

        _iv = base64.b64decode(iv)
            
        encoded_data = data.encode()
        cipher = AES.new(self.__key.encode(), AES.MODE_CBC, iv=_iv)
        padded_data = pad(encoded_data, AES.block_size)
        ciphertext = cipher.encrypt(padded_data)
        
        # Encode the ciphertext to Base64 string
        encoded_ciphertext = base64.b64encode(ciphertext).decode('utf-8')
        
        return encoded_ciphertext

    def decrypt(self, encoded_ciphertext: str, iv: bytes) -> str:
        """
        Decrypts encrypted data using AES with the private key.

        Args:
            ciphertext: The encrypted data (bytes).
            iv: The initialization vector used for encryption (bytes).

        Returns:
            The decrypted data (bytes).
        """
        ciphertext = base64.b64decode(encoded_ciphertext)

        cipher = AES.new(self.__key.encode(), AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)
        return unpad(decrypted, AES.block_size).decode()

