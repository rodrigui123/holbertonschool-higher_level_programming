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
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}")
