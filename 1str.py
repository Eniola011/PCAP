#!/usr/bin/python3
# enter a string to hide in uppercase: HIDE
string = input("Enter a word to hide in uppercase: ")
secret_string = ""
for char in string:
    secret_string += str(ord(char))
print("Secret Message: ", secret_string)

string = ""
for i in range(0, len(secret_string)-1, 2):
    charcode = secret_string[i] + secret_string[i+1]
    string += chr(int(charcode))
print("Original Message: ", string)
