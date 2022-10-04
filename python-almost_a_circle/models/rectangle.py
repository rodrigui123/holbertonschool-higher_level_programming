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

    def update(self, *args, **kwargs):
        """update the Rectangle class"""
        length = len(args)
        if length > 0:
            self.__id = args[0]
            if length > 1:
                self.__width = args[1]
            if length > 2:
                self.__height = args[2]
            if length > 3:
                self.__x = args[3]
            if length > 4:
                self.__y = args[4]
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs.get(key)
                if key == 'width':
                    self.width = kwargs.get(key)
                if key == 'height':
                    self.height = kwargs.get(key)
                if key == 'x':
                    self.x = kwargs.get(key)
                if key == 'y':
                    self.y = kwargs.get(key)

    def to_dictionary(self):
        """Rectangle instance to dictionary representation"""
        newdict = {}
        newdict['id'] = self.id
        newdict['width'] = self.width
        newdict['height'] = self.height
        newdict['x'] = self.x
        newdict['y'] = self.y
        return newdict
