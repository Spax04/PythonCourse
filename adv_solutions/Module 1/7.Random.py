import random

class LotteryTicket:
    def __init__(self):
        self.numbers = []

    def generate_numbers(self):
        self.numbers = random.sample(range(1, 51), 6)

    def check_number(self, number):
        return number in self.numbers

    def display_ticket(self):
        print("Lottery Ticket Numbers:")
        print(self.numbers)

# Example usage
ticket = LotteryTicket()
ticket.generate_numbers()

print("Checking if number 15 is on the ticket:", ticket.check_number(15))
print("Checking if number 25 is on the ticket:", ticket.check_number(25))

ticket.display_ticket()