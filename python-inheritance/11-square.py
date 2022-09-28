#!/usr/bin/python3
"""pyhton interpreter"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Write a class Rectangle that inherits
     from Rectangle (9-rectangle.py)"""
    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return (f"[Square] {self.__width}/{self.__height}")
