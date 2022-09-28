#!/usr/bin/python3
"""Write a class that inherits from list"""


class Mylist(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        my_list = self.copy()
        my_list.sort()
        print(my_list)
