import re
import json
from pathlib import Path

class LoginSystem:
    def __init__(self):
        self.users_file = "users.json"
        self.users = self._load_users()

    def _load_users(self):
        try:
            with open(self.users_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save_users(self):
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f)

    def register(self, username, password):
        if not re.match("^[a-zA-Z0-9]+$", username):
            return False, "Username must contain only letters and numbers"
        
        if username in self.users:
            return False, "Username already exists"
        
        self.users[username] = {
            "password": password,
            "data": {}  # You can store user-specific data here
        }
        self._save_users()
        return True, "Registration successful"

    def login(self, username, password):
        if username not in self.users:
            return False, "Username not found"
        
        if self.users[username]["password"] != password:
            return False, "Incorrect password"
        
        return True, self.users[username]["data"]

def main():
    login_system = LoginSystem()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, message = login_system.register(username, password)
            print(message)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, data = login_system.login(username, password)
            if success:
                print(f"Login successful! User data: {data}")
            else:
                print(f"Login failed: {data}")

        elif choice == "3":
            break

if __name__ == "__main__":
    main()