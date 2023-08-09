#!/usr/bin/python3
# a simple guessing game
secret_number = 11

while True:
    guess = int(input("Guess the secret number between 1 and 10: "))

    if guess == secret_number:
        print("You\'re right!")
        break
