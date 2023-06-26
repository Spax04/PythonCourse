# Create a class called LotteryTicket that simulates a lottery ticket. The ticket should have a list of numbers between 1 and 50 (inclusive),
# and it should provide methods to generate random numbers for the ticket, check if a given number is present on the ticket, and display the ticket's numbers.

import random


class LotteryTicket:
    def __init__(self):

    # Your code here

    def generate_numbers(self):

    # Your code here

    def check_number(self, number):

    # Your code here

    def display_ticket(self):


# Your code here

# Example usage
ticket = LotteryTicket()
ticket.generate_numbers()

print("Checking if number 15 is on the ticket:", ticket.check_number(15))
print("Checking if number 25 is on the ticket:", ticket.check_number(25))

ticket.display_ticket()
