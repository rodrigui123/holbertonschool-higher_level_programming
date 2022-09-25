#!/usr/bin/python3
"""write a class rectangle that defines a rectangle"""


class Rectangle:
    """empty class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """On instantiation"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
            return(self.__width * self.__height)

    def perimeter(self):
            if self.__width == 0 or self.__height == 0:
                return 0
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        string = ""
        for i in range(self.__height):
            if i > 0:
                string += '\n'
            for i in range(self.__width):
                string += str(self.print_symbol)
        return string

    def __repr__(self):
        string = "Rectangle(" + str(self.__width) + ", "
        string += str(self.__height) + ")"
        return string

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
