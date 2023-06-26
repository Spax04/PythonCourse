# You are now tasked with creating an advanced program for an online bookstore that includes a more complex inventory management system. The program should incorporate dictionary operations and methods, while and for loops, if and else operators, as well as functions. The program should provide additional functionality, such as calculating the total value of the inventory and generating a report based on specific criteria.
#
# The program should include the following features:
#
# 1.	Initialize an empty inventory dictionary.
# 2.	Add books to the inventory along with their titles, authors, quantities, and prices.
# 3.	Remove books from the inventory.
# 4.	Update the quantity and price of existing books in the inventory.
# 5.	Display the current inventory with detailed information for each book.
# 6.	Check if a specific book is present in the inventory.
# 7.	Calculate the total value of the inventory (quantity multiplied by price) and display it.
# 8.	Generate a report of books with quantities below a certain threshold (e.g., less than 10 copies).
#
# To make the exercise more challenging, try to modularize your code by creating functions for each operation and utilize appropriate control structures.

def display_inventory(inventory):
    print("Current Inventory:")
    for book_id, book_details in inventory.items():
        print(f"Book ID: {book_id}")
    print(f"Title: {book_details['title']}")
    print(f"Author: {book_details['author']}")
    print(f"Quantity: {book_details['quantity']}")
    print(f"Price: ${book_details['price']}")
    print("")


def check_book(inventory, book_id):
    if book_id in inventory:
        print(f"Book ID {book_id} is present in the inventory.")
    else:
        print(f"Book ID {book_id} is not present in the inventory.")


def calculate_total_value(inventory):
    total_value = 0
    for book_id, book_details in inventory.items():
        quantity = book_details['quantity']
    price = book_details['price']
    total_value += quantity * price
    print(f"Total inventory value: ${total_value}")


def generate_report(inventory, threshold):
    print(f"Books with quantities below {threshold}:")
    for book_id, book_details in inventory.items():
        quantity = book_details['quantity']
    if quantity < threshold:
        print(f"Book ID: {book_id}")
    print(f"Title: {book_details['title']}")
    print(f"Quantity: {quantity}")
    print("")


def add_book(inventory):
    book_id = input("Enter the book ID: ")
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: $"))
    book_details = {'title': title, 'author': author, 'quantity': quantity, 'price': price}
    inventory[book_id] = book_details
    print("Book added to the inventory.")


def remove_book(inventory, book_id):
    if book_id in inventory:
        del inventory[book_id]
    print(f"Book ID {book_id} removed from the inventory.")
    else:
    print(f"Book ID {book_id} is not present in the inventory.")

def update_book(inventory, book_id):
    if book_id in inventory:
        book_details = inventory[book_id]
    quantity = int(input("Enter the new quantity: "))
    price = float(input("Enter the new price: $"))
    book_details['quantity'] = quantity
    book_details['price'] = price
    print(f"Book ID {book_id} updated.")
    else:
    print(f"Book ID {book_id} is not present in the inventory.")


def inventory_management():
    inventory = {}
    while True:
        print("\nInventory Management Menu:")
        print("1. Display current inventory")
        print("2. Check if a book is in inventory")
        print("3. Calculate total inventory value")
        print("4. Generate report of books with quantities below a threshold")
        print("5. Add a book to the inventory")
        print("6. Remove a book from the inventory")
        print("7. Update a book in the inventory")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_inventory(inventory)
        elif choice == "2":
            book_id = input("Enter the book ID: ")
            check_book(inventory, book_id)
        elif choice == "3":
            calculate_total_value(inventory)
        elif choice == "4":
            threshold = int(input("Enter the quantity threshold: "))
            generate_report(inventory, threshold)
        elif choice == "5":
            add_book(inventory)
        elif choice == "6":
            book_id = input("Enter the book ID: ")
            remove_book(inventory, book_id)
        elif choice == "7":
            book_id = input("Enter the book ID: ")
            update_book(inventory, book_id)
        elif choice == "8":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

inventory_management()
