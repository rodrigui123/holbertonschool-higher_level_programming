#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    largestNum = my_list[0]
    for num in my_list:
        if num > largestNum:
            largestNum = num
    return largestNum
