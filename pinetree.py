#!/usr/bin/python3
# print a pinetree using '#'
height = int(input("How tall is your tree? "))
spaces = height - 1
hashes = 1
stump_spaces = height - 1
while height != 0:
    for space in range(spaces):
        print(' ', end="")
    for hassh in range(hashes):
        print('#', end="")
    print()

    spaces -= 1
    hashes += 2
    height -= 1

for stump in range(stump_spaces):
    print(' ', end="")

print("##")
