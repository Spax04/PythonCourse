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

    # Your code here

    def check_out(self):

    # Your code here

    def check_in(self):


# Your code here


class Book(LibraryItem):


# Your code here


class DVD(LibraryItem):


# Your code here


class Library:
    def __init__(self):

    # Your code here

    def add_item(self, item):

    # Your code here

    def remove_item(self, item):

    # Your code here

    def display_items(self):


# Your code here


# Create a library instance

# Your code here


# Add books and DVDs to the library

# Your code here


# Display all items in the library

# Your code here


# Simulate borrowing and returning items
while True:

# Your code here
