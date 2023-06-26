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


# Your code here


def remove_product(inventory, product):


# Your code here


def check_product_availability(inventory, product):


# Your code here


def update_product_quantity(inventory, product, quantity):


# Your code here


def display_out_of_stock_products(inventory):


# Your code here


def calculate_inventory_value(inventory, prices):


# Your code here


def main():
    inventory = {}
    prices = {
        "Apple": 0.5,
        "Banana": 0.3,
        "Orange": 0.4,
        "Mango": 1.0,
        "Strawberry": 0.2
    }


# Your code here


if __name__ == "__main__":
    main()
