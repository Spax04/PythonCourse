# In this exercise, we will work with dictionary operations and methods to create a program that manages a contact list. We will use dictionaries to store the contact information, including the name, phone number, and email address.
#
# Your task is to write the code that allows the user to perform the following operations on the contact list:
# •	Add a new contact.
# •	Display all contacts.
# •	Search for a contact by name.
# •	Update a contact's phone number.
# •	Remove a contact.
# •
# Once you have completed the code, test it by performing the specified operations on the contact list.

# Initialize an empty contact list dictionary
contacts = {}

# Add contacts to the list

contacts["John"] = {
"phone": "1234567890",
"email": "john@example.com"
}
contacts["Jane"] = {
"phone": "9876543210",
"email": "jane@example.com"
}

# Display all contacts

print("All Contacts:")
for name, info in contacts.items():
    print(f"Name: {name}")
    print(f"Phone: {info['phone']}")
    print(f"Email: {info['email']}")
    print()


# Search for a contact by name

search_name = "John"
if search_name in contacts:
    contact_info = contacts[search_name]
    print(f"Contact found for {search_name}:")
    print(f"Phone: {contact_info['phone']}")
    print(f"Email: {contact_info['email']}")
else:
    print(f"No contact found for {search_name}.")


# Update a contact's phone number

update_name = "John"
new_phone = "5555555555"
if update_name in contacts:
    contacts[update_name]["phone"] = new_phone
    print(f"Phone number updated for {update_name} to {new_phone}.")
else:
    print(f"No contact found for {update_name}.")


# Remove a contact

remove_name = "Jane"
if remove_name in contacts:
    del contacts[remove_name]
    print(f"{remove_name} removed from contacts.")
else:
    print(f"No contact found for {remove_name}.")

# Display the updated contact list

print("Updated Contact List:")
for name, info in contacts.items():
    print(f"Name: {name}")
    print(f"Phone: {info['phone']}")
    print(f"Email: {info['email']}")
    print()