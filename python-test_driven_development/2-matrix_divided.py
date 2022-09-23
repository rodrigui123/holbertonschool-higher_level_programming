#!/usr/bin/python3
"""python interpreter"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""

    if div is not int and div is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    counter = 0
    list = []
    for row in matrix:
        if counter != 0 and len(row) != rowSize:
            raise TypeError("Each row of the matrix must have the same size")
        rowSize = len(row)
        sublist = []
        list .append(sublist)
        for elements in row:
            sublist .append(elements)
            if type(matrix) is not list and type(matrix) is not int or type(matrix) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return list
