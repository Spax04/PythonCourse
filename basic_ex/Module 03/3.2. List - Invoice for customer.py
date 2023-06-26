# In this exercise, we will create a program that generates a customized invoice for a customer based on their purchases.
# We will use string formatting to populate the invoice template with the customer's information and item details.
#
# Your task is to write the code that takes input from the user for their name, address, and purchased items.
# Then, using string formatting, generate an invoice that includes the customer's details and itemized information.


# Prompt the user for customer information
name = input("Enter customer name: ")
address = input("Enter customer address: ")

# Prompt the user for purchased items
num_items = int(input("Enter the number of items purchased: "))

# Initialize variables
item_names = []
item_prices = []
total_price = 0

# Get item details from the user

# Your code here


# Generate the invoice using string formatting
invoice = f"""
Invoice
-------
Customer Name: {name}
Customer Address: {address}

Items Purchased:
"""

# Add itemized information to the invoice

# Your code here

# Print the generated invoice
print(invoice)
