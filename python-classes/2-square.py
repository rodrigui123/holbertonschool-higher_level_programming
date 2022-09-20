#!/usr/bin/python3
"""Creating an empty class that defines a square"""


class Square:
    """this is the empty class"""
    def __init__(self, size=0):
        """adding a private attribute """
        self.__size = size

    def __is__valid__name(self, size):
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) != int:
            raise TypeError("size must be an integer")
        return size
