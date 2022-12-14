#!/usr/bin/python3
"""Creating an empty class that defines a square"""


class Square:
    """this is the empty class"""
    def __init__(self, size=0, position=(0, 0)):
        """adding a private attribute """
        self.size = size
        self.position = position

    @property
    def size(self):
        size = self.__size
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) != 2 or
                type(value[0]) != int or type(value[1]) != int or
                (value[0]) < 0 or (value[1]) < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        if self.__size == 0:
                print()
                return
        for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                if i == self.__size - 1:
                    print(end="")
            print("#" * self.__size)

    def area(self):
        return (self.__size * self.__size)
