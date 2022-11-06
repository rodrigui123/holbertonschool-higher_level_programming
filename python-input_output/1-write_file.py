#!/usr/bin/python3
"""pyhton interpreter"""


def write_file(filename="", text=""):
    """function that writes a string to
    a text file (UTF8) and returns the
    number of characters written"""
    with open(filename, 'w') as f:
        write_file = f.write(text)
        return write_file
