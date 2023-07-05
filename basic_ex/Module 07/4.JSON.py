# In this exercise, we will create a simple program to manage a book inventory using JSON. You will implement a Python class that allows you to perform various operations such as adding books, updating book details, searching for books, and displaying the inventory.
#
# Instructions:
#
# Create a class called BookInventory.
# The class should have the following methods:
# __init__(): Initialize an empty inventory dictionary.
# add_book(title, author, quantity): Add a book to the inventory. The book details (title, author, and quantity) should be provided as arguments.
# update_book(title, author, quantity): Update the quantity of an existing book in the inventory. The book details (title, author, and quantity) should be provided as arguments.
# search_book(title): Search for a book in the inventory by its title. Return the book details if found, or a message indicating that the book was not found.
# display_inventory(): Display the current inventory with all book details.
# The inventory should be stored in a JSON file called inventory.json.
# When the BookInventory object is created, it should load the existing inventory from the JSON file (if it exists) and initialize the inventory dictionary accordingly.
# After performing any operations (addition, update), the inventory should be saved back to the JSON file.


import json

class BookInventory:
    def __init__(self):
        self.inventory = self.load_inventory()

    def load_inventory(self):
        # Your code here

    def save_inventory(self):

    # Your code here

    def add_book(self, title, author, quantity):
        # Your code here


    def update_book(self, title, author, quantity):
        # Your code here

    def search_book(self, title):
        # Your code here

    def display_inventory(self):
        # Your code here

# Example usage:
inventory = BookInventory()

inventory.add_book("The Great Gatsby", "F. Scott Fitzgerald", 5)
inventory.add_book("To Kill a Mockingbird", "Harper Lee", 3)
inventory.update_book("The Great Gatsby", "F. Scott Fitzgerald", 10)

print(inventory.search_book("To Kill a Mockingbird"))
inventory.display_inventory()