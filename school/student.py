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


def main():
    name = input("Please enter the name of the student : ")
    gradeMath = float(input("Please enter the grade in math: "))
    gradeEnglish = float(input("Please enter the grade in English: "))
    gradeSport = float(input("Please enter the grade in sport: "))
    gradeArt = float(input("Please enter the grade in Art: "))
    student = Student(name, gradeMath, gradeEnglish, gradeSport, gradeArt)

    manager = StudentManager()

    manager.addStudent(student)


main()
