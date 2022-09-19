#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDic = {}
    for key in a_dictionary.keys():
        newDic[key] = a_dictionary.get(key) * 2
    return newDic
