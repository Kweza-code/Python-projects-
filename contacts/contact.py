import json
import os


class Contact:
    def __init__(self, name, email, phone):
        name = self.name
        email = self.email
        phone = self.email

    def to_dict(self):
        data = {
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }


def display_menu():
    print("Welcome to contact manager")
    print("1: Add a new contact")
    print("2: View all contacts")
    print("3 : Exit")


def add_contact():
    name = input("Please enter the name of your new contact: ")
    email = input("Please enter the email of your new contact: ")
    phone = int(input("Please enter the phone number of your new contact"))

    contact = Contact(name, email, phone)
    file_name = "contact.json"
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="UTF-8") as file:
            try:
                contact = json.load(file)
            except json.JSONDecodeError:
                data = []

            except Exception as e:
                print(f"An error as error has occured {e} ")
