#!/usr/bin/python3
"""pyhton interpreter"""


def append_write(filename="", text=""):
    """function that appends a string at
    the end of a text file (UTF8) and returns
     the number of characters added"""
    with open(filename, 'a') as f:
        append_n = f.write(text)
        return append_n
