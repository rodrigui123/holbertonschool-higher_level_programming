#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i >= 'a' and i <= 'z':
        print("{:s}".format(i), end='')
    print(end='\n')