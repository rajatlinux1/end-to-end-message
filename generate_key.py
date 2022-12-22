import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def gen_key():
    password = b"password"
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    key = str(key).lstrip("b").lstrip("''").rstrip("''")
    key_file_object = open("key.txt", "w+")
    key_file_object.write(key)
    key_file_object.close()


if __name__ == "__main__":
    gen_key()
