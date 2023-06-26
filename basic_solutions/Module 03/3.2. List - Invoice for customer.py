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

for i in range(num_items):
item_name = input(f"Enter the name of item {i+1}: ")
item_price = float(input(f"Enter the price of item {i+1}: "))
item_names.append(item_name)
item_prices.append(item_price)
total_price += item_price


# Generate the invoice using string formatting
invoice = f"""
Invoice
-------
Customer Name: {name}
Customer Address: {address}

Items Purchased:
"""

# Add itemized information to the invoice

for i in range(num_items):
invoice += f"{i+1}. {item_names[i]} - ${item_prices[i]:.2f}\n"

invoice += f"\nTotal Price: ${total_price:.2f}"

# Print the generated invoice
print(invoice)
