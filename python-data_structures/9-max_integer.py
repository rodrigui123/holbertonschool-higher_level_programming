#!/usr/bin/python3
def max_integer(my_list=[]):
    largestNum = my_list[:1]
    for num in my_list:
        if num > largestNum:
            largestNum = num
    return num
