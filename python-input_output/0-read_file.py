#!/usr/bin/python3
"""pyhton interpreter"""


def read_file(filename=""):
    """function that reads a text file
     (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding="UTF8") as f:
        read_file = f.read()
        print(read_file, end="")
