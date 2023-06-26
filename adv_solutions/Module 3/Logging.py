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
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        logging.info(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            logging.info(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            logging.warning(f"Withdrawal failed. Insufficient funds in account {self.account_number}. Balance: {self.balance}")

# Example usage
account1 = Account("123456789", 5000)
account2 = Account("987654321", 10000)

account1.deposit(2000)
account2.withdraw(15000)
account1.withdraw(4000)


# In this exercise, we created a simple banking application with a Banking class that represents a bank account. The class has three methods:
#
# __init__(self, account_number, balance): This method initializes a bank account with an account number and a starting balance.
#
# deposit(self, amount): This method allows depositing an amount into the account. It increases the account balance and logs the deposit event along with the account number, deposited amount, and new balance.
#
# withdraw(self, amount): This method allows withdrawing an amount from the account if sufficient funds are available. It decreases the account balance and logs the withdrawal event along with the account number, withdrawn amount, and new balance. If the withdrawal amount exceeds the account balance, a warning is logged instead.
#
# We configured the logging system to log messages to a file named banking.log at the INFO level. The log messages include the timestamp, log level, and a custom message format.
#
# We created two instances of the Account class and demonstrated the usage of the deposit() and withdraw() methods. Each method logs relevant information such as the account number, amount, and new balance.