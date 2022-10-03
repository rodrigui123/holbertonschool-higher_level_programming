#!/usr/bin/python3
"""python interpreter"""


from models.base import Base
"""import class: base"""


class Rectangle(Base):
    """class: inherit rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor (width, height, x, y"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        width = self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value

    @property
    def height(self):
        height = self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.__height = value

    @property
    def x(self):
        x = self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        y = self.__y

    @y.setter
    def y(self, value):
        self.__y = value
