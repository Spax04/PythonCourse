# You are tasked with creating a simple program that simulates a cashier in a grocery store. The program should take input from the user for the prices and quantities of various items, calculate the total cost, and then display the result. Additionally, the program should redirect the output to a file for record-keeping purposes.
#
# Your task is to create a Python class called Cashier that implements this program. The class should have the following functionalities:
#
# 1.	A method called take_input() that prompts the user to enter the price and quantity of each item. The method should store this information in appropriate data structures.
# 2.	A method called calculate_total() that calculates the total cost of all the items based on their prices and quantities.
# 3.	A method called display_result() that displays the total cost to the user.
# 4.	A method called redirect_output() that redirects the output to a file named "receipt.txt" instead of displaying it to the console. The file should be created if it doesn't exist, and if it does exist, it should be overwritten.


import sys


class Cashier:
    def __init__(self):
        self.items = []

    def take_input(self):

    # Your code here

    def calculate_total(self):

    # Your code here

    def display_result(self):

    # Your code here

    def redirect_output(self):


# Your code here


# Usage example:
cashier = Cashier()
cashier.take_input()
cashier.display_result()
cashier.redirect_output()

