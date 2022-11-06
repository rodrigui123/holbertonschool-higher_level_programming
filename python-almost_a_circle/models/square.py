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
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """adding values to atttributes"""
        length = len(args)
        if length > 0 or length is None:
            self.id = args[0]
            if length > 1:
                self.size = args[1]
            if length > 2:
                self.x = args[2]
            if length > 3:
                self.y = args[3]
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs.get(key)
                if key == 'size':
                    self.size = kwargs.get(key)
                if key == 'x':
                    self.x = kwargs.get(key)
                if key == 'y':
                    self.y = kwargs.get(key)

    def to_dictionary(self):
        """Square instance to dictionary representation"""
        newdict = {}
        newdict['id'] = self.id
        newdict['size'] = self.size
        newdict['x'] = self.x
        newdict['y'] = self.y
        return newdict
