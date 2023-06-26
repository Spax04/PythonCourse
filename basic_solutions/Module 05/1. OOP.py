# You are tasked with creating a simple program to manage a library system. The library contains various types of items, including books and DVDs. Each item has a unique identifier, title, and availability status. Your task is to implement a class hierarchy to represent these items and manage their availability.
#
# Requirements:
#
# 1.	Create a base class called "LibraryItem" that has the following attributes:
# •	id (integer): Unique identifier for the item.
# •	title (string): Title of the item.
# •	available (boolean): Indicates whether the item is available for borrowing or not.
# 2.	Create two subclasses, "Book" and "DVD," that inherit from the "LibraryItem" class.
# •	The "Book" class should have an additional attribute called "author" (string).
# •	The "DVD" class should have an additional attribute called "director" (string).
# 3.	Implement a method called "check_out" in the "LibraryItem" class that sets the "available" attribute to False when an item is borrowed.
#
# 4.	Implement a method called "check_in" in the "LibraryItem" class that sets the "available" attribute to True when an item is returned.
#
# 5.	Create a class called "Library" that has the following attributes:
#
# •	items (list): A list to store all the items in the library.
# 6.	Implement the following methods in the "Library" class:
#
# •	add_item(item): Adds the given item to the library's item list.
# •	remove_item(item): Removes the given item from the library's item list.
# •	display_items(): Displays the details of all items in the library.
# 7.	Create an instance of the "Library" class and add some books and DVDs to it.
#
# 8.	Use a loop to simulate a user borrowing and returning items from the library. Prompt the user to enter the ID of the item they want to borrow or return. If the item is available, borrow it, and if it's already borrowed, return it. Display appropriate messages to the user based on the item's availability.

class LibraryItem:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.available = True

    def check_out(self):
        if self.available:
            self.available = False
            print(f"{self.title} (ID: {self.id}) has been borrowed.")
        else:
            print(f"{self.title} (ID: {self.id}) is already borrowed.")

    def check_in(self):
        if not self.available:
            self.available = True
            print(f"{self.title} (ID: {self.id}) has been returned.")
        else:
            print(f"{self.title} (ID: {self.id}) is already available.")


class Book(LibraryItem):
    def __init__(self, id, title, author):
        super().__init__(id, title)
        self.author = author


class DVD(LibraryItem):
    def __init__(self, id, title, director):
        super().__init__(id, title)
        self.director = director


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display_items(self):
        print("Library Items:")
        for item in self.items:
            if isinstance(item, Book):
                print(f"Book - ID: {item.id}, Title: {item.title}, Author: {item.author}, Available: {item.available}")
            elif isinstance(item, DVD):
                print(
                    f"DVD - ID: {item.id}, Title: {item.title}, Director: {item.director}, Available: {item.available}")


# Create a library instance
library = Library()

# Add books and DVDs to the library
book1 = Book(1, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")
dvd1 = DVD(3, "The Shawshank Redemption", "Frank Darabont")
dvd2 = DVD(4, "The Godfather", "Francis Ford Coppola")

library.add_item(book1)
library.add_item(book2)
library.add_item(dvd1)
library.add_item(dvd2)

# Display all items in the library
library.display_items()

# Simulate borrowing and returning items
while True:
    print("\nLibrary Menu:")
    print("1. Borrow an item")
    print("2. Return an item")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        item_id = int(input("Enter the ID of the item you want to borrow: "))
        for item in library.items:
            if item.id == item_id:
                item.check_out()
                break
        else:
            print("Item not found.")

    elif choice == "2":
        item_id = int(input("Enter the ID of the item you want to return: "))
        for item in library.items:
            if item.id == item_id:
                item.check_in()
                break
        else:
            print("Item not found.")

    elif choice == "3":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")