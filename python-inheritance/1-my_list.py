#!/usr/bin/python3
"""python interpreter"""


class Mylist(list):
    """Write a class that inherits from list"""
    def print_sorted(self):
        my_list = self.copy()
        my_list.sort()
        print(my_list)
        return my_list
