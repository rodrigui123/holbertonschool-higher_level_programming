#!/usr/bin/python3
for i in range(97, 123):
    letter = chr(i)
    chr(i) = letter[65:-71]
    print("{}".format(letter), end="")
