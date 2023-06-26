# You are a manager at a grocery store and you need to keep track of the inventory of various products. Your task is to create a program that allows you to perform set operations and methods on the inventory. The program should have the following functionalities:
#
# 1.	Add a product to the inventory.
# 2.	Remove a product from the inventory.
# 3.	Check if a product is available in the inventory.
# 4.	Update the quantity of a product in the inventory.
# 5.	Display the list of products that are out of stock.
# 6.	Calculate the total value of the inventory.
#
# To accomplish this, you need to create a menu-driven program that provides options to perform these operations. The program should continue executing until the user chooses to exit.

def add_product(inventory, product, quantity):
    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity
    print(f"{quantity} {product}(s) added to the inventory.")


def remove_product(inventory, product):
    if product in inventory:
        del inventory[product]
    print(f"{product} removed from the inventory.")
    else:
    print(f"{product} is not available in the inventory.")


def check_product_availability(inventory, product):
    if product in inventory:
        print(f"{product} is available in the inventory.")
    else:
        print(f"{product} is not available in the inventory.")


def update_product_quantity(inventory, product, quantity):
    if product in inventory:
        inventory[product] = quantity
    print(f"Quantity of {product} updated to {quantity}.")
    else:
    print(f"{product} is not available in the inventory.")


def display_out_of_stock_products(inventory):
    out_of_stock = [product for product, quantity in inventory.items() if quantity == 0]
    if out_of_stock:
        print("Products out of stock:")
    for product in out_of_stock:
        print(product)
    else:
        print("All products are in stock.")


def calculate_inventory_value(inventory, prices):
    total_value = 0
    for product, quantity in inventory.items():
        if product in prices:
            price = prices[product]
    total_value += price * quantity
    print(f"Total inventory value: ${total_value:.2f}")


def main():
    inventory = {}
    prices = {
        "Apple": 0.5,
        "Banana": 0.3,
        "Orange": 0.4,
        "Mango": 1.0,
        "Strawberry": 0.2
    }


while True:
    print("\nGrocery Store Inventory Management Menu:")
    print("1. Add product to inventory")
    print("2. Remove product from inventory")
    print("3. Check product availability")
    print("4. Update product quantity")
    print("5. Display out-of-stock products")
    print("6. Calculate inventory value")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter the product name: ")
        quantity = int(input("Enter the quantity: "))
        add_product(inventory, product, quantity)
    elif choice == "2":
        product = input("Enter the product name: ")
        remove_product(inventory, product)
    elif choice == "3":
        product = input("Enter the product name: ")
        check_product_availability(inventory, product)
    elif choice == "4":
        product = input("Enter the product name: ")
        quantity = int(input("Enter the new quantity: "))
        update_product_quantity(inventory, product, quantity)
    elif choice == "5":
        display_out_of_stock_products(inventory)
    elif choice == "6":
        calculate_inventory_value(inventory, prices)
    elif choice == "7":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
