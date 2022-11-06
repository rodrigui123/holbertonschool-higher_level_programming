#!/usr/bin/python3
"""python interpreter"""


def print_square(size):
    """prints a square with the character #"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for i in range(size):
            if i == size - 1:
                print(end="")
        print("#" * size)
