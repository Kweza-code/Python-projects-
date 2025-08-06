import json

def test():
    data = []

    name = input("Enter the name: ")
    username = input("Enter the username: ")

    contact = {
        "name": name,
        "username": username
    }

    data.append(contact)

    jsonFile = input("Please enter a name of a json file (e.g., data.json): ")

    with open(jsonFile, "w") as file:
        json.dump(data, file, indent=4)  # Save the list, not just contact

    with open(jsonFile, "r") as file:
        contents = file.read()

    infos = json.loads(contents)

    for info in infos:
        name = info["name"]
        print(name)

test()
        