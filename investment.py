#!/usr/bin/python3
# Ask user for amount to invest and interest expected
amount = float(input("How much do you intend to invest? "))
rate = (float(input("What rate were you given? "))) * 0.01
# cycle through 10 years
for yr in range(10):
    amount = amount + (amount * rate)
# output end results
print("Investment after 10 years: {:.2f}".format(amount))
