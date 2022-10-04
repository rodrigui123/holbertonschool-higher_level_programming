#!/usr/bin/python3
"""python interpreter"""


from models.rectangle import Rectangle
"""import class: Rectangle"""


class Square(Rectangle):
    """class: Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.__height = value
