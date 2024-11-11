import os
import argparse
from cryptography.fernet import Fernet

## Skapar nyckeln som vi kommer att använda för att krypera samt dekryptera filer ##
def generate_key():
    key = Fernet.generate_key()
    with open("Secret.key", "wb") as key_file:
        key_file.write(key)
        print("Key has been generated!")
        return key

## Hämtar nyckeln så att dem andra funktionerna kan använda den ##
def load_key():
    with open('Secret.key', "rb") as key_file:
        return key_file.read()

##  Funktionen som krypterar filen med nyckeln ##
def encrypt_file(filename, key):
    cipher_suite = Fernet(key)

    with open(filename, 'rb') as file:
        file_data = file.read()

    encrypted_data = cipher_suite.encrypt(file_data) 

    with open(f"{filename}.encrypted", 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    file_path = filename
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} har blivit raderad! ")
    else:
        print(f"{file_path} finns inte! ")

    # with open(filename, 'wb') as encrypted_file:
    #     encrypted_file.write(encrypted_data)

    print(f"File '{filename}' har blivit krypterad! ")       


## Funktionen som dekrypterar filen med nyckeln ## 
def decrypt_file(encrypted_filename, key):
    cipher = Fernet(key)

    with open(encrypted_filename,'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = cipher.decrypt(encrypted_data)
    original_filename = encrypted_filename.replace('.encrypted', '')

    with open(original_filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

        ## Test code ##
        file_path = encrypted_filename
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} har blivit raderad! ")
    else:
        print(f"{file_path} finns inte! ")
        ## Test code ##

    print(f"Fil {encrypted_file} har blivit dekrypterad")

## Argparse delen av koden som tar hand om dem olika alternativen :)
parser = argparse.ArgumentParser(description="Mitt Krypteringsverktyg som slutprojekt i Applied script")
parser.add_argument("action", choices=["encrypt", "decrypt", "generate-key"], help="Välj ett alternativ")
parser.add_argument("filename", nargs="?", help="Ange den fil du vill kryptera!")
args = parser.parse_args()

## Kollar igenom vad du vill göra och svarar enligt alternativet ##
if args.action == "generate-key":
    generate_key()
elif args.action == "encrypt":
    key = load_key()
    if args.filename:
        encrypt_file(args.filename, key)
    else:
        print("Ange ett filnamn för att kryptera!")

elif args.action == "decrypt":
    key = load_key()
    if args.filename:
        decrypt_file(args.filename, key)
    else:
        print("Ange ett filnamn för att kryptera!")
        
