#!/usr/bin/python3
"""Creating an empty class that defines a square"""


from ctypes import sizeof


class Square:
    """this is the empty class"""
    def __init__(self, size=0):
        """adding a private attribute """
        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        self.area = self.__size * self.__size
    return (self.area)
