#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        printed = ""
        for i in range(0, x):
            print(f"{my_list[i]}", end="")
            printed += 1
    except:
        pass
    return printed
