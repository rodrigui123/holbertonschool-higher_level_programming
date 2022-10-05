#!/usr/bin/python3
"""python interpreter"""


import json


class Base(list):
    """class: Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        newlist = []
        if list_objs is not None:
            for obj in list_objs:
                newlist.append(cls.to_dictionary())
        with open(f"{cls.__name__}.json", "w") as f:
            f.write(cls.to_json_string(newlist))
