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
        try:
            with open('inventory.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_inventory(self):
        with open('inventory.json', 'w') as file:
            json.dump(self.inventory, file)

    def add_book(self, title, author, quantity):
        if title in self.inventory:
            print(f"The book '{title}' already exists in the inventory.")
        else:
            self.inventory[title] = {'author': author, 'quantity': quantity}
            self.save_inventory()
            print(f"The book '{title}' has been added to the inventory.")

    def update_book(self, title, author, quantity):
        if title in self.inventory:
            self.inventory[title]['author'] = author
            self.inventory[title]['quantity'] = quantity
            self.save_inventory()
            print(f"The book '{title}' has been updated.")
        else:
            print(f"The book '{title}' does not exist in the inventory.")

    def search_book(self, title):
        if title in self.inventory:
            book_details = self.inventory[title]
            return f"Book: {title}\nAuthor: {book_details['author']}\nQuantity: {book_details['quantity']}"
        else:
            return f"The book '{title}' was not found in the inventory."

    def display_inventory(self):
        print("Current Inventory:")
        if self.inventory:
            for title, details in self.inventory.items():
                print(f"Book: {title}\nAuthor: {details['author']}\nQuantity: {details['quantity']}")
        else:
            print("Inventory is empty.")

# Example usage:
inventory = BookInventory()

inventory.add_book("The Great Gatsby", "F. Scott Fitzgerald", 5)
inventory.add_book("To Kill a Mockingbird", "Harper Lee", 3)
inventory.update_book("The Great Gatsby", "F. Scott Fitzgerald", 10)

print(inventory.search_book("To Kill a Mockingbird"))
inventory.display_inventory()