import json
import os
import bcrypt
import getpass


file_name = "contact.json"


class Contact:
    def __init__(self, username, password):

        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password
        }


def validPassword(inputPassword):
    has_upper = any(char.isupper() for char in inputPassword)
    has_special = any(char in "!@#$%&*" for char in inputPassword)
    digit_count = sum(char.isdigit() for char in inputPassword)

    if has_upper and has_special and digit_count >= 3:
        return True
    else:
        print("Your password don't respect")
        return False


def createAccount(file_name):

    username = input("Please enter a username: ")
    inputPassword = getpass.getpass("Please enter a password: ")
    validPassword(inputPassword)
    hash = bcrypt.gensalt()

    password = bcrypt.hashpw(inputPassword.encode(), hash).decode()

    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = []
    else:
        data = []

    c = Contact(username, password)

    data.append(c.to_dict())

    with open(file_name, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4)

        print("Your account has been created ")


def connectAccount(file_name):

    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = []
    else:
        print("There is no account created, please create an account first.")
        return

    print("Veuillez vous connecter")

    usernameConnection = input("Veuillez entrer votre username de connexion: ")
    passwordConnection = getpass.getpass(
        "Please enter your password: ").encode()

    for account in data:
        if usernameConnection == account["username"]:
            stored_password = account["password"].encode()
            if bcrypt.checkpw(passwordConnection, stored_password):
                print("✅ Access granted")
                return
            else:
                print("❌ Incorrect password")
                return

    print("❌ Username not found")


def main():
    file_name = "contact.json"
    print("1: Create an account: ")
    print("2: Connect into an account: ")
    action = int(input("Please choose your action: "))

    while True:
        if action == 1:
            createAccount(file_name)
            break
        else:
            connectAccount(file_name)
            break


main()
