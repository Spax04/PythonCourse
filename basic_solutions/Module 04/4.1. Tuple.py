# You are working at a grocery store, and your manager has assigned you a task to manage the inventory of fruits. You need to create a program that allows you to perform various operations on a tuple containing the names of different fruits. Your program should provide a menu-based interface for the user to select and perform different operations.
#
# Here are the operations you need to implement:
#
# 1.	Print the list of fruits.
# 2.	Check if a specific fruit is present in the list.
# 3.	Count the number of occurrences of a specific fruit.
# 4.	Find the index of a specific fruit.
# 5.	Sort the fruits in alphabetical order.
# 6.	Exit the program.
#
# Instructions:
#
# 1.	Create a tuple called "fruits" containing at least 5 different fruit names.
# 2.	Display a menu to the user with the available operations (1-6).
# 3.	Based on the user's choice, perform the corresponding operation.
# 4.	Use a while loop to repeatedly display the menu until the user chooses to exit (option 6).
#
# Hints:
#
# •	You can use a for loop to iterate over the fruits tuple for certain operations.
# •	Use if and else statements to handle different menu choices.
# •	You can define separate functions for each operation to keep the code organized and modular.


def print_fruits(fruits):
    print("Fruits:", ", ".join(fruits))

def check_fruit(fruits):
    if fruit in fruits:
        print(f"The fruit '{fruit}' is present in the list.")
    else:
        print(f"The fruit '{fruit}' is not present in the list.")


def count_fruit(fruits):
    count = fruits.count(fruit)
    print(f"The fruit '{fruit}' occurs {count} time(s) in the list.")


def find_index(fruits):
    try:
        index = fruits.index(fruit)
        print(f"The fruit '{fruit}' is found at index {index}.")
    except ValueError:
        print(f"The fruit '{fruit}' is not present in the list.")


def sort_fruits(fruits):
    sorted_fruits = sorted(fruits)
    print("Sorted fruits:", ", ".join(sorted_fruits))


fruits = ("apple", "banana", "orange", "grape", "kiwi")

while True:
    print("\nMenu:")
    print("1. Print the list of fruits")
    print("2. Check if a specific fruit is present")
    print("3. Count the number of occurrences of a specific fruit")
    print("4. Find the index of a specific fruit")
    print("5. Sort the fruits in alphabetical order")
    print("6. Exit the program")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        print_fruits(fruits)
    elif choice == "2":
        fruit = input("Enter the fruit name: ")
        check_fruit(fruits, fruit)
    elif choice == "3":
        fruit = input("Enter the fruit name: ")
        count_fruit(fruits, fruit)
    elif choice == "4":
        fruit = input("Enter the fruit name: ")
        find_index(fruits, fruit)
    elif choice == "5":
        sort_fruits(fruits)
    elif choice == "6":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
