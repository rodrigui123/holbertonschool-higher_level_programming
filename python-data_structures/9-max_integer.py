#!/usr/bin/python3
def max_integer(my_list=[]):
    largestNum = my_list[0]
    if my_list == "":
        return None
    for num in my_list:
        if num > largestNum:
            largestNum = num
    return largestNum
