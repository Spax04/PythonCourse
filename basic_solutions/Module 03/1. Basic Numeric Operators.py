# Imagine you are a teacher and you want to create a program to help your students practice basic arithmetic operations. The program should present the user with a menu of options to choose from: addition, subtraction, multiplication, or division. Once the user selects an option, the program should ask for two numbers and perform the chosen operation on them. The result should then be displayed to the user.
#
# Here are the steps to follow:
# •	Display a menu of options to the user: addition, subtraction, multiplication, and division.
# •	Ask the user to enter their choice by selecting a number corresponding to the desired operation.
# •	Based on the user's choice, ask the user to enter two numbers.
# •	Use if-else statements to determine which operation to perform based on the user's choice.
# •	Perform the chosen operation on the two numbers.
# •	Display the result to the user

print("Welcome to the Arithmetic Practice Program!")
print("Please select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
operation = "+"
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 + num2
elif choice == 2:
operation = "-"
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 - num2
elif choice == 3:
operation = "*"
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 * num2
elif choice == 4:
operation = "/"
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 / num2
else:
print("Invalid choice. Please try again.")
exit()

print(f"\nResult: {num1} {operation} {num2} = {result}")

