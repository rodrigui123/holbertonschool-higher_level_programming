#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", number, "is" end="")
if number % 10 > 5:
    print()