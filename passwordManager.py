#A password locker program by Nwogu Kennedy.

import os
import getpass
from cryptography.fernet import Fernet
import json
import hashlib

# Function to hash master password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to save the master password to a file
def save_master_password(master_password):
    hashed_password = hash_password(master_password)
    with open("master_password.json", 'w') as file:
        json.dump({"master_password": hashed_password}, file)

# Function to load the master password from a file
def load_master_password():
    try:
        with open("master_password.json","r") as file:
            data = json.load(file)
            return data.get("master_password")
    except:
        return None

# Function to verify master password
def verify_master_password():
    stored_hashed_password = load_master_password()
    
    if not stored_hashed_password:
        print("No master password set. Please create one.")
        master_password = getpass.getpass("Set your master password: ")
        save_master_password(master_password)
        print("Master password set. Please restart the program.")
        return False
    
    master_password = getpass.getpass("Enter your master password: ")
    
    if hash_password(master_password) == stored_hashed_password:
        print("Access granted.")
        return True
    else:
        print("Access denied. Invalid master password.")
        return False    

# Function to generate or load encryption key
def load_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key

# Encrypt the password using the encryption key
def encrypt_password(password, fernet):
    return fernet.encrypt(password.encode())

# Decrypt the password using the encryption key
def decrypt_password(encrypted_password, fernet):
    return fernet.decrypt(encrypted_password).decode()

# Save passwords to a file
def save_passwords(passwords, fernet):
    with open("passwords.json", "w") as file:
        encrypted_data = {k: fernet.encrypt(v.encode()).decode() for k, v in passwords.items()}
        json.dump(encrypted_data, file)

# Load passwords from a file
def load_passwords(fernet):
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            encrypted_data = json.load(file)
            return {k: fernet.decrypt(v.encode()).decode() for k, v in encrypted_data.items()}
    else:
        return {}

# Main function to handle password manager operations
def password_manager():
    key = load_key()
    fernet = Fernet(key)
    passwords = load_passwords(fernet)

    while True:
        print("\nPassword Manager")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Delete a password")
        print("4. List all passwords")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            service = input("Enter the service name: ")
            password = getpass.getpass("Enter the password: ")
            passwords[service] = password
            save_passwords(passwords, fernet)
            print(f"Password for {service} added successfully.")

        elif choice == "2":
            service = input("Enter the service name: ")
            if service in passwords:
                print(f"Password for {service}: {passwords[service]}")
            else:
                print(f"No password found for {service}")

        elif choice == "3":
            service = input("Enter the service name: ")
            if service in passwords:
                del passwords[service]
                save_passwords(passwords, fernet)
                print(f"Password for {service} deleted.")
            else:
                print(f"No password found for {service}")

        elif choice == "4":
            if passwords:
                print("Stored passwords:")
                for service in passwords.keys():
                    print(service)
            else:
                print("No passwords stored.")

        elif choice == "5":
            print("Exiting password manager.")
            break

        else:
            print("Invalid choice. Please choose again.")

# Check if the script is run directly or not imported as a module 
if __name__ == "__main__":
    if verify_master_password():
        password_manager()
    else:
        print("Exiting the program...")    
