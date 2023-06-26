# You work at a grocery store and have been assigned a task to create a program that calculates the total cost of a customer's purchase. Your program should allow the user to enter the quantity and price per item for different grocery items and calculate the subtotal, tax, and total cost of the purchase. Additionally, the program should provide a discount based on the total cost if it exceeds a certain threshold.
#
# Here are the steps to follow:
#
# 1.	Define a function called calculate_subtotal that takes two parameters: quantity and price_per_item. Inside the function, calculate the subtotal by multiplying the quantity by the price per item and return it.
# 2.	Use a while loop to repeat the following operations until the user chooses to exit:
# •	Ask the user to enter the name of the grocery item.
# •	Ask the user to enter the quantity of the item.
# •	Ask the user to enter the price per item.
# •	Call the calculate_subtotal function with the quantity and price per item as arguments to calculate the subtotal.
# •	Add the subtotal to a running total.
# •	Display the subtotal to the user.
# •	Repeat the above steps for multiple grocery items.
# •	After all items are entered, calculate the tax by multiplying the total cost by the tax rate (e.g., 0.08 for 8% tax).
# •	Calculate the total cost by adding the tax to the total cost.
# •	Apply a discount of 10% if the total cost exceeds a certain threshold (e.g., $100).
# •	Display the tax, discount (if applicable), and final total cost to the user.


# Make ‘calculate_subtotal’ function here

print("Welcome to the Grocery Store!\n")

# User input for grocery items
item_count = 1
grocery_total = 0
grocery_items = []

while True:

    item_name = input(f"Enter the name of item {item_count}: ")
    quantity = int(input("Enter the quantity: "))
    price_per_item = float(input("Enter the price per item: "))
    subtotal = calculate_subtotal(quantity, price_per_item)
    grocery_total += subtotal

    print(f"Subtotal for {item_name}: ${subtotal:.2f}")

    grocery_items.append((item_name, quantity, price_per_item))

    choice = input("Do you want to add more items? (yes/no): ")
    if choice.lower() != "yes":
        break
# Calculating tax

    tax_rate = 0.08
    tax = grocery_total * tax_rate

# Calculating total cost

    total_cost = grocery_total + tax


# Applying discount if the total cost exceeds a certain threshold

    discount_threshold = 100
    discount_percentage = 0.1
    discount = 0

    if total_cost > discount_threshold:
    discount = total_cost * discount_percentage
    total_cost -= discount
# Displaying the results

    print("\n-----Receipt-----")
    for item in grocery_items:
    item_name, quantity, price_per_item = item
    print(f"{item_name}: {quantity} x ${price_per_item:.2f}")
    print("-----------------")
    print(f"Subtotal: ${grocery_total:.2f}")
    print(f"Tax: ${tax:.2f}")

    if discount > 0:
    print(f"Discount: ${discount:.2f}")

    print(f"Total Cost: ${total_cost:.2f}")

    print("\nThank you for shopping at the Grocery Store!")