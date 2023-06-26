# Let's imagine you are working on a program for a library management system. In this exercise, you will create a class called Book that represents a book in the library. The Book class will have the following functionalities:
#
# 1.	It should be able to track the number of times a book has been borrowed.
# 2.	It should have a method called display that prints the book's title, author, and the number of times it has been borrowed.
# 3.	It should have a method called borrow that increments the borrow count by 1 each time it is called.
#
# To make things more interesting, you need to implement decorators to add additional functionalities to the Book class. Here are the decorators you need to implement:
#
# 1.	time_taken_decorator: This decorator should calculate and print the time taken to execute any method of the Book class.
# 2.	authenticate_decorator: This decorator should prompt the user to enter a password before executing any method of the Book class. The password should be passed as an argument to the decorator.
# 3.	log_decorator: This decorator should log the name of the method being executed.
#
# Your task is to implement the Book class and the decorators described above. Make sure to use lambda functions, composition of decorators, and passing arguments to decorators where necessary.

import time


def time_taken_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        print("Time taken:", time_taken, "seconds")
        return result
    return wrapper


def authenticate_decorator(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            entered_password = input("Enter password: ")
            if entered_password == password:
                return func(*args, **kwargs)
            else:
                print("Authentication failed. Access denied.")
        return wrapper

    return decorator


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Executing method:", func.name)
        return func(*args, **kwargs)
    return wrapper


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrow_count = 0

    @log_decorator
    @authenticate_decorator("secret")
    @time_taken_decorator
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Borrow Count:", self.borrow_count)

    @log_decorator
    @authenticate_decorator("secret")
    @time_taken_decorator
    def borrow(self):
        self.borrow_count += 1
        print("Book borrowed. Borrow Count:", self.borrow_count)

# Test the Book class and decorators
book = Book("The Great Gatsby", "F. Scott Fitzgerald")
book.display()
print()
book.borrow()
book.borrow()
