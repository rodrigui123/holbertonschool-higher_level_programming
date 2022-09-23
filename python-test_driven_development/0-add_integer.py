#!/usr/bin/python3
"""python interpreter"""


def add_integer(a, b=98):
    """python adding 2 integers"""

    if a is None or a is not int or a is not float:
        raise TypeError("a must be an integer")
    if b is not int or b is not float:
         raise TypeError("b must be an integer")
    return int(a) + int(b)
