import json


class Student:
    def __init__(self, name, gradeMath, gradeEnglish, gradeSport, gradeArt):
        self.name = name
        self.gradeMath = gradeMath
        self.gradeEnglish = gradeEnglish
        self.gradeSport = gradeSport
        self.gradeArt = gradeArt

    def to_dict(self):
        return {
            "name": self.name,
            "gradeMath": self.gradeMath,
            "gradeEnglish": self.gradeEnglish,
            "gradeSport": self.gradeSport,
            "gradeArt": self.gradeArt
        }


class StudentManager:
    def __init__(self, file_name="student.json"):
        self.file_name = file_name

    def addStudent(self, student):
        try:
            with open(self.file_name, "r") as file:
                students = json.load(file)
        except FileNotFoundError:
            students = []

        students.append(student.to_dict())

        with open(self.file_name, "w") as file:
            json.dump(students, file, indent=4)

    def viewAllStudent(self):
        try:
            with open(self.file_name, "r") as file:
                students = json.load(file)
        except FileNotFoundError:
            print("There are no students registered.")
            return

        for idx, student in enumerate(students):
            print(f"Student number {idx + 1}: {student['name']}")
            print(f"  Math: {student['gradeMath']}")
            print(f"  English: {student['gradeEnglish']}")
            print(f"  Sport: {student['gradeSport']}")
            print(f"  Art: {student['gradeArt']}")
            print()


def main():
    print("Welcome to Student Manager")
    print("Please choose an action:")
    print("1: Add a student with grades")
    print("2: View all students with their grades")
    print("3: Exit")

    manager = StudentManager()

    while True:
        action = input("Enter your choice (1, 2 or 3): ")

        if action == "1":
            name = input("Please enter the name of the student: ")
            try:
                gradeMath = float(input("Please enter the grade in math: "))
                gradeEnglish = float(
                    input("Please enter the grade in English: "))
                gradeSport = float(input("Please enter the grade in sport: "))
                gradeArt = float(input("Please enter the grade in Art: "))
            except ValueError:
                print("Invalid input for grades. Please enter numeric values.")
                continue

            student = Student(name, gradeMath, gradeEnglish,
                              gradeSport, gradeArt)
            manager.addStudent(student)
            print(f"Student {name} added successfully.\n")

        elif action == "2":
            manager.viewAllStudent()

        elif action == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
