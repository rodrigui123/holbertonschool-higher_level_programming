#!/usr/bin/python3
"""pyhton interpreter"""


import json


def load_from_json_file(filename):
    """function that creates an Object
    from a “JSON file”"""
    with open(filename, 'r'):
        return json.load(f)
