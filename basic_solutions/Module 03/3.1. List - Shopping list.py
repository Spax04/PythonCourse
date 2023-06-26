# In this exercise, we will work with string formatting and list operations to create a program that manages a shopping list. We will use string formatting to display the shopping list and perform various operations on it using list methods.
#
# Your task is to write the code that allows the user to perform the following operations on a shopping list:
#
# Add items to the shopping list.
# Remove items from the shopping list.
# Display the current shopping list.
# Once you have completed the code, test it by performing the specified operations on the shopping list.


# Initialize an empty shopping list
shopping_list = []

while True:
    print("Menu:")
    print("1. Add item to shopping list")
    print("2. Remove item from shopping list")
    print("3. Display shopping list")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"Item '{item}' added to the shopping list.")

    elif choice == "2":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Item '{item}' removed from the shopping list.")
        else:
            print(f"Item '{item}' not found in the shopping list.")

    elif choice == "3":
        print("Shopping List:")
        if len(shopping_list) == 0:
            print("The shopping list is empty.")
        else:
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")

    elif choice == "4":
        print("Thank you for using the shopping list manager!")
        break

    else:
        print("Invalid choice. Please try again.")


print("Thank you for using the shopping list manager!")

