# You are now challenged to create a more advanced program that simulates a contact management system using dictionaries, while and for loops, if and else operators, and functions. The program should allow users to perform various operations on a contact list, including adding, removing, updating, and searching for contacts. Additionally, the program should provide functionality to sort and display the contacts based on specific criteria.
#
# The program should include the following features:
#
# 1.	Initialize an empty contact list dictionary.
# 2.	Add contacts to the list along with their names, phone numbers, and email addresses.
# 3.	Remove contacts from the list.
# 4.	Update the phone number and email address of existing contacts.
# 5.	Display the current contact list with detailed information for each contact.
# 6.	Search for a specific contact by name and display their information.
# 7.	Sort and display the contact list alphabetically by name or by phone number.
#
# To make the exercise more challenging, try to modularize your code by creating functions for each operation and utilize appropriate control structures.

def display_contacts(contacts):
    print("Current Contact List:")
    for contact_id, contact_details in contacts.items():
        print(f"Contact ID: {contact_id}")
    print(f"Name: {contact_details['name']}")
    print(f"Phone Number: {contact_details['phone']}")
    print(f"Email Address: {contact_details['email']}")
    print("")

def search_contact(contacts, name):
    found_contacts = []
    for contact_id, contact_details in contacts.items():
        if name.lower() in contact_details['name'].lower():
            found_contacts.append(contact_details)
    if found_contacts:
        print("Search Results:")
    for contact in found_contacts:
        print(f"Name: {contact['name']}")
    print(f"Phone Number: {contact['phone']}")
    print(f"Email Address: {contact['email']}")
    print("")
    else:
    print(f"No contacts found with the name '{name}'.")


def sort_contacts(contacts, sort_criteria):
    sorted_contacts = sorted(contacts.values(), key=lambda x: x[sort_criteria])
    print("Sorted Contact List:")
    for contact in sorted_contacts:
        print(f"Name: {contact['name']}")
    print(f"Phone Number: {contact['phone']}")
    print(f"Email Address: {contact['email']}")
    print("")


def add_contact(contacts):
    contact_id = input("Enter the contact ID: ")
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contact_details = {'name': name, 'phone': phone, 'email': email}
    contacts[contact_id] = contact_details
    print("Contact added to the list.")


def remove_contact(contacts, contact_id):
    if contact_id in contacts:
        del contacts[contact_id]
    print(f"Contact ID {contact_id} removed from the list.")
    else:
    print(f"Contact ID {contact_id} is not present in the list.")


def update_contact(contacts, contact_id):
    if contact_id in contacts:
        contact_details = contacts[contact_id]
    phone = input("Enter the new phone number: ")
    email = input("Enter the new email address: ")
    contact_details['phone'] = phone
    contact_details['email'] = email
    print(f"Contact ID {contact_id} updated.")
    else:
    print(f"Contact ID {contact_id} is not present in the list.")


def contact_management():
    contacts = {}
    while True:
        print("\nContact Management Menu:")
        print("1. Display current contact list")
        print("2. Search for a contact")
        print("3. Sort and display the contact list")
        print("4. Add a contact")
        print("5. Remove a contact")
        print("6. Update a contact")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            name = input("Enter the name to search: ")
            search_contact(contacts, name)
        elif choice == "3":
            sort_criteria = input("Enter the sort criteria (name or phone): ")
            sort_contacts(contacts, sort_criteria)
        elif choice == "4":
            add_contact(contacts)
        elif choice == "5":
            contact_id = input("Enter the contact ID to remove: ")
            remove_contact(contacts, contact_id)
        elif choice == "6":
            contact_id = input("Enter the contact ID to update: ")
            update_contact(contacts, contact_id)
        elif choice == "7":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


contact_management()
