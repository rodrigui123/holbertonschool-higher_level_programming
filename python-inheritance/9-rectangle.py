#!/usr/bin/python3
"""pyhton interpreter"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Write a class Rectangle that inherits
     from BaseGeometry (7-base_geometry.py)"""
    def __init__(self, width, height):
        """constructor (width, height)"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
