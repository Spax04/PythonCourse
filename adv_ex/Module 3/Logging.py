# Create a Python program that demonstrates logging in a real-world scenario.
# Imagine you are developing a simple banking application that consists of multiple modules.
# Your task is to create a logging system that logs important events and actions within the application.
# The logging should include logging to a file, logging from multiple modules, and logging variable data.
# Implement the logging system using the built-in logging module in Python.

import logging

# Configure logging to file
logging.basicConfig(filename='banking.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Account:
    def __init__(self, account_number, balance):
        # Your code here

    def deposit(self, amount):
        # Your code here

    def withdraw(self, amount):
        # Your code here

# Example usage
account1 = Account("123456789", 5000)
account2 = Account("987654321", 10000)

account1.deposit(2000)
account2.withdraw(15000)
account1.withdraw(4000)