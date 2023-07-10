# You are tasked with creating a Python class that interacts with a MySQL database to perform CRUD (Create, Read, Update, Delete) operations on a table called "employees". The "employees" table has the following columns: id (integer), name (string), and salary (float).
#
# Your task is to implement the following methods in the class:
#
# create_employee: Accepts the employee's name and salary as arguments and inserts a new record into the "employees" table.
# get_employee: Accepts an employee ID as an argument and retrieves the corresponding employee's name and salary from the "employees" table.
# update_employee: Accepts an employee ID, name, and salary as arguments and updates the corresponding employee's record in the "employees" table.
# delete_employee: Accepts an employee ID as an argument and deletes the corresponding employee's record from the "employees" table.
# Note: Make sure to establish a connection to the MySQL database and handle any necessary error cases.

import mysql.connector

class EmployeeManager:
    def __init__(self, host, user, password, database):
        # Your code here

    def create_employee(self, name, salary):
        # Your code here

    def get_employee(self, employee_id):

    # Your code here

    def update_employee(self, employee_id, name, salary):

    # Your code here

    def delete_employee(self, employee_id):

    # Your code here

    def __del__(self):
        # Your code here

# Usage example
manager = EmployeeManager('localhost', 'your_username', 'your_password', 'your_database')

manager.create_employee('John Doe', 5000.0)
manager.create_employee('Jane Smith', 6000.0)

manager.get_employee(1)
manager.get_employee(2)

manager.update_employee(1, 'John Smith', 5500.0)
manager.update_employee(3, 'Invalid Employee', 0.0)  # Employee not found

manager.delete_employee(2)
manager.delete_employee(3)  # Employee not found