# You are working as a manager at a clothing store, and you need to create a program to manage the inventory of different clothing items. Your program should allow you to perform various operations on a tuple of clothing items, such as adding new items, updating quantities, and generating sales reports. The program should provide a menu-based interface for the user to select and perform different operations.
#
# Here are the operations you need to implement:
#
# 1.	Print the list of clothing items and their quantities.
# 2.	Check if a specific clothing item is in stock.
# 3.	Update the quantity of a specific clothing item.
# 4.	Generate a sales report for a specific clothing item.
# 5.	Add a new clothing item to the inventory.
# 6.	Exit the program.
#
# Instructions:
#
# •	Create a tuple called "inventory" containing at least 5 different clothing items as tuples. Each clothing item tuple should consist of the item name and its quantity.
# •	Display a menu to the user with the available operations (1-6).
# •	Based on the user's choice, perform the corresponding operation.
# •	Use a while loop to repeatedly display the menu until the user chooses to exit (option 6).
#
# Hints:
#
# •	Use a for loop to iterate over the inventory tuple for certain operations.
# •	You can use if and else statements to handle different menu choices.
# •	To update the quantity of a specific item, you can convert the inventory tuple to a list, update the quantity, and then convert it back to a tuple.

def print_inventory(inventory):
    print("Inventory:")
    for item, quantity in inventory:
        print(f"{item}: {quantity}")

def check_stock(inventory):
    for clothing_item, quantity in inventory:
        if clothing_item == item:
            print(f"The item '{item}' is in stock.")
    return
    print(f"The item '{item}' is not in stock.")

def update_quantity(inventory):
    updated_inventory = list(inventory)
    for i, (clothing_item, old_quantity) in enumerate(updated_inventory):
        if clothing_item == item:
            updated_inventory[i] = (clothing_item, quantity)
    print(f"Updated the quantity of '{item}' to {quantity}.")
    return tuple(updated_inventory)
    print(f"The item '{item}' is not in stock.")
    return inventory

def generate_sales_report(inventory):
    for clothing_item, quantity in inventory:
        if clothing_item == item:
            print(f"Sales report for '{item}':")
    print(f"Quantity in stock: {quantity}")
    return
    print(f"The item '{item}' is not in stock.")

def add_item(inventory):
    updated_inventory = list(inventory)
    updated_inventory.append((item, quantity))
    print(f"Added '{item}' to the inventory with a quantity of {quantity}.")
    return tuple(updated_inventory)

inventory = (
    ("T-Shirt", 20),
    ("Jeans", 10),
    ("Dress", 15),
    ("Sweater", 12),
    ("Jacket", 8)
)

while True:
    print("\nMenu:")
    print("1. Print the inventory")
    print("2. Check if an item is in stock")
    print("3. Update the quantity of an item")
    print("4. Generate a sales report for an item")
    print("5. Add a new item to the inventory")
    print("6. Exit the program")
    choice = input("\nEnter your choice: ")

    if choice == "1":
        print_inventory(inventory)
    elif choice == "2":
        item = input("Enter the item name: ")
        check_stock(inventory, item)
    elif choice == "3":
        item = input("Enter the item name: ")
        quantity = int(input("Enter the new quantity: "))
        inventory = update_quantity(inventory, item, quantity)
    elif choice == "4":
        item = input("Enter the item name: ")
        generate_sales_report(inventory, item)
    elif choice == "5":
        item = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        inventory = add_item(inventory, item, quantity)
    elif choice == "6":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
