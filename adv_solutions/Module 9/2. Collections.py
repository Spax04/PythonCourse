# You have been assigned a task to create a simple contact management system that can store and manipulate contact information. Each contact will have a name, phone number, and email address. To implement this, you will make use of the UserDict, UserList, and UserString classes in Python.
#
# Your task is to create a class called ContactManager that will inherit from UserDict, UserList, and UserString to store and manage contacts.
#
# The ContactManager class should have the following methods:
#
# 1.	add_contact(name, phone_number, email): Adds a new contact to the contact manager. The method should create a dictionary with the contact information and add it to the data attribute inherited from UserDict.
#
# 2.	remove_contact(name): Removes a contact from the contact manager based on the name. The method should remove the contact from the data attribute inherited from UserDict.
#
# 3.	get_contacts(): Returns a list of all contacts stored in the contact manager. The method should return the data attribute inherited from UserDict.
#
# 4.	get_contact_names(): Returns a list of names of all contacts stored in the contact manager. The method should return the data attribute inherited from UserDict.
#
# 5.	get_contact_count(): Returns the number of contacts stored in the contact manager. The method should return the length of the data attribute inherited from UserDict.

from collections import UserDict, UserList, UserString


class ContactManager(UserDict, UserList, UserString):
    def add_contact(self, name, phone_number, email):
        contact = {
            'name': name,
            'phone_number': phone_number,
            'email': email
        }
        self.data[name] = contact

    def remove_contact(self, name):
        del self.data[name]

    def get_contacts(self):
        return list(self.data.values())

    def get_contact_names(self):
        return list(self.data.keys())

    def get_contact_count(self):
        return len(self.data)


# Testing the ContactManager class
cm = ContactManager()

# Adding contacts
cm.add_contact('John Doe', '123456789', 'john.doe@example.com')
cm.add_contact('Jane Smith', '987654321', 'jane.smith@example.com')
cm.add_contact('Alice Brown', '555555555', 'alice.brown@example.com')

# Getting contacts

print(cm.get_contacts())

# [{'name': 'John Doe', 'phone_number': '123456789', 'email': 'john.doe@example.com'},
# {'name': 'Jane Smith', 'phone_number': '987654321', 'email': 'jane.smith@example.com'},
# {'name': 'Alice Brown', 'phone_number': '555555555', 'email': 'alice.brown@example.com'}]


# Removing a contact
cm.remove_contact('John Doe')

# Getting updated contacts and contact count

print(cm.get_contacts())

# [{'name': 'Jane Smith', 'phone_number': '987654321', 'email': 'jane.smith@example.com'},
# {'name': 'Alice Brown', 'phone_number': '555555555', 'email': 'alice.brown@example.com'}]

print(cm.get_contact_count()) # 2
