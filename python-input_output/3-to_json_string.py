#!/usr/bin/python3
"""pyhton interpreter"""
import json


def to_json_string(my_obj):
    """function that returns the JSON
    representation of an object (string)"""
    return json.dump(my_obj)
