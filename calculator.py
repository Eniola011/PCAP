#!/usr/bin/python3
# Simple Calculator
# Ask user for two numbers and operator
num1, operator, num2 = input("Enter numbers you want to calculate: ").split()
# convert input numbers to integers
num1, num2 = int(num1), int(num2)
# print the result of the calculation
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
else:
    print("enter a valid number and operator")
