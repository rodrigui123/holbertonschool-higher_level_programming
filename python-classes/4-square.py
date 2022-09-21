#!/usr/bin/python3
"""Creating an empty class that defines a square"""


class Square:
    """this is the empty class"""
    def __init__(self, size=0):
        """adding a private attribute """
        self.__size = size

    @property
    def size(self):
        size = self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        self.area = self.__size * self.__size
        return (self.area)

