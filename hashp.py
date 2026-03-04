import hashlib
import os
import re
class user:
    def __init__(self, username, password_hash):
        self.username=username
        self.password_hash=password_hash

class passwordsecurity:
    def check_strength(password):
        "validate password strength"
        if len(password)<8:
            return False,"password must be at least 8 characters."
        if not re.search(r"[A-Z]", password):
            return False, "password must contain an uppecase letter."
        if not re.search(r"[a-z]", password):
            return False, "password must contain a lowercase letter."
        if not re.search(r"[0-9]", password):
            return False, "password must contain a numbeer."
        return true, "strong password."

    def hash_password(password):
        salt=os.urandom(16)
        hashed=hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            salt,
            100000
            )
        return salt+hashed

    def verify_password(stored_password, entered_password):
        salt=stored_password[:16]
        stored_hash=stored_password[16:]
        new_hash=hashlib.pbkdf2_hmac(
            'sha256',
            entered_password.encode(),
            salt,
            100000
            )
        return new_hash==stored_hash

class authenticationsystem:
    
    def __init__ (self):
        self.user={}

        #register user
    def register(self, username, password):
        if username in self.user:
            print("username already exists.")
            return

        valid, message= passwordsecurity.check_strength(password)
        print(message)

        if not valid:
            return

        hashed_password=passwordsecurity.hash_password(password)

        #store hashed password 
        self.user[username]=user(username, hashed_password)
        print("user registered securely.")

        #authenticate login
        def login(self,username, password):

            if username not in self.user:
                print("user not found.")
                return
            user=self.user[username]

            if passwordsecurity.verify_password(user.password_hash, password):
                print("Auntheticatation successful. Access granted.")
            else:
                print("Authentication failed. Incorrect password.")

auth=authenticationsystem()

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice=input("choose option:")

    if choice=="1":
         username=input("Enter username:")
         password=input("Enter password:")
         auth.register(username,password)

    elif choice=="2":
        usename=input("Enter username:")
        password=input("Enter password:")
        auth.login(username, password)

    elif choice=="3":
        print("System exited securely.")
        break
    
    
         
     
    

    
            
    

    
