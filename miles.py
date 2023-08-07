#!/usr/bin/python3
# Problem: receive miles and convert to kilometers
# kilometers = mile * 1.60934

m = input("Enter miles: ")
km = int(m) * 1.60934
print("{} miles equals {:0.2f} kilometers".format(m, km))
