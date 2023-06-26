# You are tasked with creating a class to represent a bank account. The class should have the following functionalities:
#
# 1.	The account should keep track of the account holder's name and the current balance.
# 2.	It should have a method called "deposit" that allows depositing money into the account.
# 3.	The deposit amount should be a positive number. If a negative or zero amount is provided, it should raise a custom exception called "InvalidDepositAmountError" with the message "Invalid deposit amount: <amount>".
# 4.	It should have a method called "withdraw" that allows withdrawing money from the account.
# 5.	The withdrawal amount should be a positive number and should not exceed the current balance. If a negative amount is provided or the withdrawal amount exceeds the balance, it should raise a custom exception called "InsufficientFundsError" with the message "Insufficient funds for withdrawal: <amount>".
# 6.	The class should implement exception handling and a finally block to ensure that the account balance is always updated correctly, even if an exception is raised.

class InvalidDepositAmountError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidDepositAmountError(f"Invalid deposit amount: {amount}")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidDepositAmountError(f"Invalid withdrawal amount: {amount}")
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds for withdrawal: {amount}")
        self.balance -= amount

    def get_balance(self):
        return self.balance


# Test the BankAccount class
account = BankAccount("John Doe", 1000)
print(account.get_balance()) # Output: 1000

account.deposit(500)
print(account.get_balance()) # Output: 1500

account.withdraw(200)
print(account.get_balance()) # Output: 1300

try:
account.deposit(-100)
except InvalidDepositAmountError as e:
print(str(e)) # Output: Invalid deposit amount: -100

try:
account.withdraw(2000)
except InsufficientFundsError as e:
print(str(e)) # Output: Insufficient funds for withdrawal: 2000

