#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    result = sum(set(my_list))
    return result
