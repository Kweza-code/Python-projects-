import json
import os

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


def createAccount():
    file_name = "contact.json"
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")

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

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def connectAccount(file_name):

    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
        except json.jSONDecodeError:
            data = []

    else:
        print("There is no account create, please create an account")

    print("Veuillez vous conecter")

    while True:
        usernameConnection = input(
            "Veuiller entrer votre username de connection :")
        passwordConnection = input("Please enter the password : ")
        for i, value in enumerate(data):
            if usernameConnection == value["username"] and passwordConnection == value["password"]:

                return print("Access granted")

        else:
            print("An error has occured Try again")


connectAccount(file_name)
