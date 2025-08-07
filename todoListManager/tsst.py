import json


class Users:

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def to_dictt(self):
        return {
            "username": self.username,
            "password": self.password
        }


class UserManager:

    def __init__(self, file_user="users.json"):
        self.file_user = file_user

    def createUser(self, user):
        try:
            with open(self.file_user, "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = []

        users.append(user.to_dictt())

        with open(self.file_user, "w") as file:
            json.dump(users, file, indent=4)

    def connectionUser(self):
        try:
            with open(self.file_user, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print("No user file found.")
            return False

        connectionUsername = input(
            "Please enter the username for connection: ")
        connectionPassword = input(
            "Please enter the password of your username: ")

        for user in users:
            if connectionUsername == user["username"] and connectionPassword == user["password"]:
                print("✅ Access granted")
                return connectionUsername

        print("❌ Invalid credentials")
        return False


class Task:
    def __init__(self, name, description, statut):

        self.name = name
        self.description = description
        self.statut = statut

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "statut": self.statut
        }


class TaskManager:

    def __init__(self, username, file_name="task.json"):
        self.username = username
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, "r") as file:
                all_tasks = json.load(file)
                return all_tasks.get(self.username, [])
        except FileNotFoundError:
            return []

    def save_tasks(self):
        try:
            with open(self.file_name, "r") as file:
                all_tasks = json.load(file)
        except FileNotFoundError:
            all_tasks = {}

        all_tasks[self.username] = self.tasks

        with open(self.file_name, "w") as file:
            json.dump(all_tasks, file, indent=4)
            print("✅ Task saved:")

    def add_tasks(self, task):
        self.tasks.append(task.to_dict())

    def view_tasks(self):
        if not self.tasks:
            return print("There is not tasks")
        else:
            for task in self.tasks:

                print(task)


def main():
    print("Welcome to Task Manager. Please create an account or connect.")
    print("1: Create an account")
    print("2: Connect to your account")

    user_manager = UserManager()

    while True:
        try:
            choice_user = int(input("Enter your choice (1 or 2): "))
            if choice_user == 1:
                username = input("Please enter the username: ")
                password = input("Please enter the password: ")
                user = Users(username, password)
                user_manager.createUser(user)
                connected_username = username
                break
            elif choice_user == 2:
                connected_username = user_manager.connectionUser()
                if connected_username:
                    break
            else:
                continue
        except ValueError:
            print("Please enter a valid number.")

    task_manager = TaskManager(username=connected_username)

    while True:
        print("\n1: Add a new task")
        print("2: View all tasks")
        print("3: Exit")

        try:
            choice = int(input("Please choose an option: "))
            if choice == 1:
                name = input("Enter the name of the task: ")
                description = input("Enter the description of your task: ")
                statut = input("Please enter the status of your task: ")

                task = Task(name, description, statut)
                task_manager.add_tasks(task)
                task_manager.save_tasks()

            elif choice == 2:
                task_manager.view_tasks()

            elif choice == 3:
                print("Exiting Task Manager. Goodbye!")
                break

            else:
                print("Invalid choice. Please choose 1, 2, or 3.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
