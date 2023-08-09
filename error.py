#!/usr/bin/python3
# examples of error handling
while True:
    try:
        number = eval(input("Please enter your favourite number: "))
        print("Your favourite number is {:d}".format(number))
        break
    except ValueError:
        print("This is not a number")
    except: # do not use 'except' bare as it is not reliable
        print("There seems to be an error")

print("Thank you for your time.")
