#!/usr/bin/python3
# check important birthdays using logical operators
# Ask the user for their age
age = eval(input("What is your age? "))
# is age greater than or equal to 1 and age less than or equal to 18?
if (age >= 1) and (age <= 18):
    print("Important Birthday!")
# is age 21 or 50?
elif (age == 21) or (age == 50):
    print("Important Birthday!")
# is age less than 65?, if true convert to false.
elif not(age < 65):
    print("Important Birthday!")
# anything else not important!!
else:
    print("Not important!")
