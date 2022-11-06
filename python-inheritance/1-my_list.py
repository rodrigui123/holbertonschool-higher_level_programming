#!/usr/bin/python3
"""Write a class that inherits from list"""


class MyList(list):
    """"class: MyList (inherits from list)"""
    def print_sorted(self):
        new_list = self.copy()
        new_list.sort()
        print(new_list)
