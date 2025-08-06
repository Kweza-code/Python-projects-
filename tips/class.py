import json


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):

        file_name = input("Please enter the file you want to register : ")
        with open(file_name, "w") as file:
            data = {
                "title": self.title,
                "author": self.author,
                "pages": self.pages
            }
            json.dump(data, file, indent=4)


# Ask user for input when creating the object (outside the class)
title = input("Please enter the name of the book: ")
author = input("Please enter the author of the book: ")
pages = int(input("Please enter how many pages the book has: "))

# Create the Book object
my_book = Book(title, author, pages)

# Call the method
my_book.description()
