# You have been hired by a local restaurant to develop a menu management system. The restaurant owner wants you to create a program that allows the staff to add, edit, and delete menu items. Your task is to write a Python program that implements the following features:
#
# •	Display the menu options to the user: "Add item", "Edit item", "Delete item", "Display menu", and "Quit".
# •	Use a while loop to keep the program running until the user chooses to quit.
# •	Use if-else statements to execute the corresponding operation based on the user's choice.
# •	For the "Add item" option, prompt the user to enter the name of the menu item and add it to the menu.
# •	For the "Edit item" option, prompt the user to enter the name of the menu item they want to edit and then the new name for the item.
# •	For the "Delete item" option, prompt the user to enter the name of the menu item they want to delete and remove it from the menu.
# •	For the "Display menu" option, print out all the menu items.
# •	If the user enters an invalid choice, display an error message.
# •	Remember to use string operations and methods, while and for loops, if and else operators, and functions to implement this program.

def display_menu():
    print("Menu Options:")
    print("1. Add item")
    print("2. Edit item")
    print("3. Delete item")
    print("4. Display menu")
    print("5. Quit")


def add_item(menu):
    item = input("Enter the name of the menu item: ")
    menu.append(item)
    print(f"Item '{item}' added to the menu.")


def edit_item(menu):
    item = input("Enter the name of the menu item to edit: ")
    if item in menu:
        new_item = input("Enter the new name for the menu item: ")
        index = menu.index(item)
        menu[index] = new_item
        print(f"Menu item '{item}' has been edited to '{new_item}'.")
    else:
        print("Menu item not found.")


def delete_item(menu):
    item = input("Enter the name of the menu item to delete: ")
    if item in menu:
        menu.remove(item)
        print(f"Menu item '{item}' has been deleted.")
    else:
        print("Menu item not found.")


def display_menu_items(menu):
    if menu:
        print("Menu:")
        for item in menu:
            print(item)
    else:
        print("The menu is currently empty.")


menu = []
choice = 0

while choice != 5:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_item(menu)
    elif choice == 2:
        edit_item(menu)
    elif choice == 3:
        delete_item(menu)
    elif choice == 4:
        display_menu_items(menu)
    elif choice == 5:
        print("Thank you for using the menu management system. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

print("Program exited.")