#!/usr/bin/python3
"""pyhton interpreter"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of,
     or if the object is an instance of a class that
      inherited from, the specified class, otherwise False"""
    if type(object) is a_class or issubclass(type(obj), a_class):
        return True
    return False