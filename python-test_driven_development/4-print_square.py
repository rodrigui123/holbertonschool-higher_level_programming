#!/usr/bin/python3
"""python interpreter"""


def print_square(size):
    """prints a square with the character #"""

    for i in range(size):
        for i in range(size):
            if i == size -1:
                print(end="")
        print("#" * size)
