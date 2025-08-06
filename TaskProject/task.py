import os
import json


class Task:
    def __init__(self, description, due_date, status):
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }


def menu_display():

    print("Welcome in Task Manager")
    print("1: Add a task")
    print("2: View your task")
    print("3: Exit the app ")


def addTask(file_name):

    description = input("Please enter a description of your task")
    due_date = int(input("Please enter days until it needs to be done"))
    status = input("Please enter the status of your task")

    t = Task(description, due_date, status)

    if os.path.exists(file_name):
        with open(file_name, "r") as file:

            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(t.to_dict())

    with open(file_name, "w") as file:
        json.dump(data, file)


def viewAll(file_name):

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print("There is no data")
                return

        if not data:
            print("There is no task to display.")
        else:
            for i, value in enumerate(data):

                print(f"{i}: {value}")

            action = int(
                input("Please enter the number of the task you want to change: "))

            if 0 <= action < len(data):
                newStatut = input("Please enter the new statut of the task: ")
                data[action]["status"] = newStatut
            else:
                print("Invalid task number.")

            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)

    else:
        print("There is no data ")


def main():
    menu_display()
    file_name = "task.json"

    while True:
        action = input("Please enter the number : ")

        if action == "1":
            addTask(file_name)

        elif action == "2":
            viewAll(file_name)


main()
