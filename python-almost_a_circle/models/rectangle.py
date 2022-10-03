#!/usr/bin/python3
"""python interpreter"""
from models.base import Base


class Rectangle(Base):
    """class: inherit rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None)
        """class constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
