#!/usr/bin/python3
"""python interpreter"""


from models.base import Base
"""import class: base"""


class Rectangle(Base):
    """class: inherit rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor (width, height, x, y"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        """return str"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
                f" - {self.__width}/{self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returning area"""
        return (self.__width * self.__height)

    def display(self):
        """display #"""
        if self.__width == 0 or self.__height == 0:
            print()
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for r in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def update(self, *args):
        """update the Rectangle class"""
        if len(args) != 0:
            for i in len(args):
                if i > args[1]:
                    i = self.id
                if i > args[2]:
                    i = self.width
                if i > args[3]:
                    i == self.height
                if i > args[4]:
                    i == self.x
                if i > args[5]:
                    i == self.y
