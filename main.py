#!/usr/bin/python3
import sys

if len(sys.argv) != 3:
    print("Invalid arguments")
    sys.exit()

numbers = list(map(int, sys.argv[1].split(',')))
target = int(sys.argv[2])

pairs = []

for number in numbers:
    if (target - number) in numbers and (target - number) != number and ((number, target - number) and (target - number, number) not in pairs):
        pairs.append((number, target - number))

print(pairs)
