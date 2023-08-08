#!/usr/bin/python3
# Problem: get even numbers or odd numbers
# use a for loop and conditionals
for n in range(1, 21):
    if (n % 2 != 0):
        print("{} is an odd number".format(n))
    else:
        print("{} is an even number".format(n))
