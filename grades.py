#!/usr/bin/python3
# Problem: group users into their respective class/grade
# Ask the user for their age
age = eval(input("What is your age? "))
# is the user age 5?
if (age == 5):
    print("Go to kindergarten.")
# is the user between age 6 to 17?
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to {} grade".format(grade))
# is user age greater than 17?
else:
    print("Go to College.")
