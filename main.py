from cryptography.fernet import Fernet
import base64
import os
import time

key = ""
with open("key.txt", "r") as f:
    key = f.readline()
f.close()

if not key:
    print("key generating...")
    os.system('python generate_key.py')
    time.sleep(2)
    with open("key.txt", "r") as f:
        key = f.readline()
    f.close()

fernet = Fernet(key)


def read_message(msg):
    msg = bytes(msg, "utf-8")
    decMessage = fernet.decrypt(msg).decode()
    print("Decrypted : ", decMessage)


def write_message(msg):
    encMessage = fernet.encrypt(msg.encode())
    print("Encrypted : ", str(encMessage).lstrip("b"))


looping = True

while looping:
    option = int(input("1 : Read Message\n2 : Write Message\n>> "))

    if option == 1:
        message = input("Paste or Type Message here : ")
        read_message(message)
        looping = False

    elif option == 2:
        message = input("Paste or Type Message here : ")
        write_message(message)
        looping = False

    else:
        print("Please choose 1 or 2")
