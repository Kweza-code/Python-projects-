import json
import os


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }


def display_menu():
    print("Welcome to contact manager")
    print("1: Add a new contact")
    print("2: View all contacts")
    print("3 : Exit")


def add_contact(file_name):
    file_name = "contact.json"
    name = input("Please enter the name of your new contact: ")
    email = input("Please enter the email of your new contact: ")
    phone = int(input("Please enter the phone number of your new contact"))

    contact = Contact(name, email, phone)

    if os.path.exists(file_name):
        with open(file_name, "r", encoding="UTF-8") as file:
            try:
                datas = json.load(file)
            except json.JSONDecodeError:
                datas = []

            except Exception as e:
                print(f"An error as error has occured {e} ")

    datas.append(contact.to_dict())

    with open(file_name, "w", encoding="UTF-8") as file:
        json.dump(datas, file, indent=4)

    print("Contact added with sucesss")


def viewAll(file_name):

    if os.path.exists(file_name):
        with open(file_name, "r", encoding="UTF-8") as file:
            datas = json.load(file)

    for idx, data in enumerate(datas, start=1):
        print(f"{idx}: {data}")


def main():

    file_name = "contact.json"

    while True:
        display_menu()

        try:
            action = int(input("Please enter a number : "))
            if action == 1:
                add_contact(file_name)
            elif action == 2:
                viewAll(file_name)
            elif action == 3:
                print("Good Bye See you soon")
                return

        except Exception as e:
            (f"An error has occured {e}")


main()
