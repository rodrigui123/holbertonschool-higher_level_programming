#!/usr/bin/python3
"""pyhton interpreter"""


class BaseGeometry:
    """Empty class"""
    def area(self):
        raise Exception('area() is not implemented')


    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("age must be an integer")
        if value <= 0:
            raise ValueError("age must be greater than 0")
