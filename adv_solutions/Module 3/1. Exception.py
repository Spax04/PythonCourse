# Let's level up the calculator application you developed earlier. In addition to performing basic mathematical operations, the calculator should now support advanced calculations involving exponentiation and square root. However, you need to handle multiple types of exceptions that may occur during these calculations.
#
# The Calculator class should have the following methods:
#
# 1.	add(x, y): This method should take two numbers, x and y, as input and return their sum.
#
# 2.	subtract(x, y): This method should take two numbers, x and y, as input and return the result of subtracting y from x.
#
# 3.	multiply(x, y): This method should take two numbers, x and y, as input and return their product.
#
# 4.	divide(x, y): This method should take two numbers, x and y, as input and return the result of dividing x by y. Handle the ZeroDivisionError exception if y is zero and return a meaningful error message.
#
# 5.	exponentiation(x, y): This method should take two numbers, x and y, as input and return the result of raising x to the power of y. Handle the TypeError exception if either x or y is not a valid number and return a meaningful error message.
#
# 6.	square_root(x): This method should take a number x as input and return the square root of x. Handle the ValueError exception if x is negative and return a meaningful error message.


import math


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    def exponentiation(self, x, y):
        try:
            return x ** y
        except TypeError:
            return "Error: Invalid input. Both x and y should be numbers."

    def square_root(self, x):
        try:
            if x < 0:
                raise ValueError("Error: Cannot calculate square root of a negative number.")
            return math.sqrt(x)
        except ValueError as e:
            return str(e)


# Test the Calculator class
calculator = Calculator()
print(calculator.add(2, 3)) # Output: 5
print(calculator.subtract(5, 2)) # Output: 3
print(calculator.multiply(4, 3)) # Output: 12
print(calculator.divide(10, 2)) # Output: 5.0
print(calculator.divide(7, 0)) # Output: Error: Cannot divide by zero.
print(calculator.exponentiation(2, 3)) # Output: 8
print(calculator.exponentiation(2, 'a')) # Output: Error: Invalid input. Both x and y should be numbers.
print(calculator.square_root(16)) # Output: 4.0
print(calculator.square_root(-9)) # Output: Error: Cannot calculate square root of a negative number.
