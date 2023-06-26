# You are tasked with creating a ticket booking system using object-oriented programming (OOP) principles in Python. The system should allow users to book tickets for various events, display event details, manage ticket availability, and calculate total ticket prices. Implement inheritance and composition to create specialized classes for different types of events and ticket categories.
#
# In this exercise, we have defined three classes: Event, TicketCategory, and Ticket. The Event class represents an event with attributes for its name, venue, date, and time. It also maintains a list of available ticket categories. The TicketCategory class represents a category of tickets with attributes for its name and price. The Ticket class represents a ticket for a specific event and ticket category.
#
# The TicketBookingSystem class is responsible for managing events, ticket categories, and ticket bookings. It has methods to add events, display events, book tickets, display tickets, and calculate the total price of all booked tickets.
#
# In the example usage section, we create a TicketBookingSystem object and add two events with their ticket categories. We display the event list, book tickets for different events and ticket categories, display the ticket list, and calculate the total price of all booked tickets.

class Event:
    def __init__(self, name, venue, date, time):
        self.name = name
        self.venue = venue
        self.date = date
        self.time = time
        self.ticket_categories = []

    def __str__(self):
        return f"Event: {self.name}\nVenue: {self.venue}\nDate: {self.date}\nTime: {self.time}"

    def add_ticket_category(self, ticket_category):
        self.ticket_categories.append(ticket_category)

    def display_ticket_categories(self):
        print(f"Ticket Categories for {self.name}:")
        for category in self.ticket_categories:
            print(category)

class TicketCategory:
    def init(self, name, price):
        self.name = name

    self.price = price

    def __str__(self):
        return f"Category: {self.name}\nPrice: {self.price}"


class Ticket:
    def init(self, event, category):
        self.event = event
        self.category = category

    def __str__(self):
        return f"Event: {self.event.name}\nCategory: {self.category.name}\nPrice: {self.category.price}"


class TicketBookingSystem:
    def init(self):
        self.events = []
        self.tickets = []

    def add_event(self, event):
        self.events.append(event)

    def display_events(self):
        print("Events:")
        for event in self.events:
            print(event)

    def book_ticket(self, event, ticket_category):
        if ticket_category in event.ticket_categories:
            ticket = Ticket(event, ticket_category)
            self.tickets.append(ticket)
            print(f"Ticket booked: {ticket}")
        else:
            print(f"Ticket category {ticket_category.name} is not available for event {event.name}")

    def display_tickets(self):
        print("Booked Tickets:")
        for ticket in self.tickets:
            print(ticket)

    def calculate_total_price(self):
        total_price = sum(ticket.category.price for ticket in self.tickets)
        return total_price

# Example usage
booking_system = TicketBookingSystem()

event1 = Event("Music Concert", "Stadium A", "2023-07-15", "20:00")
event2 = Event("Theater Play", "Theater B", "2023-07-20", "19:30")

category1 = TicketCategory("General", 50)
category2 = TicketCategory("VIP", 100)

event1.add_ticket_category(category1)
event2.add_ticket_category(category1)
event2.add_ticket_category(category2)

booking_system.add_event(event1)
booking_system.add_event(event2)

booking_system.display_events()

booking_system.book_ticket(event1, category1)
booking_system.book_ticket(event2, category1)
booking_system.book_ticket(event2, category2)

booking_system.display_tickets()

total_price = booking_system.calculate_total_price()
print(f"Total Price: {total_price}")

