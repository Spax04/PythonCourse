
# In this exercise, we will work with tuples to create a program that manages a simple product inventory. We will use tuples to store the product information, including the product name, price, and quantity.
#
# Your task is to write the code that performs the following operations on the product inventory without using a menu:
# •	Add products to the inventory.
# •	Display the current inventory.
# •	Update the quantity of a product.
# •	Remove products from the inventory.
#
# Once you have completed the code, test it by performing the specified operations on the product inventory.

# Initialize an empty product inventory
inventory = []

# Add products to the inventory

inventory.append(("Apple", 0.5, 10))
inventory.append(("Banana", 0.25, 15))
inventory.append(("Orange", 0.35, 20))

# Display the current inventory

print("Current Inventory:")
for product in inventory:
name, price, quantity = product
print(f"Product: {name}, Price: {price}, Quantity: {quantity}")

# Update the quantity of a product

update_product = "Apple"
new_quantity = 5
for i, product in enumerate(inventory):
name, price, quantity = product
if name == update_product:
inventory[i] = (name, price, new_quantity)
print(f"Quantity of {update_product} updated to {new_quantity}.")
break


# Remove products from the inventory

remove_product = "Banana"
for product in inventory:
name, price, quantity = product
if name == remove_product:
inventory.remove(product)
print(f"{remove_product} removed from the inventory.")
break


# Display the updated inventory

print("Updated Inventory:")
for product in inventory:
name, price, quantity = product
print(f"Product: {name}, Price: {price}, Quantity: {quantity}")
