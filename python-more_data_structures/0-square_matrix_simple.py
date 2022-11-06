#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    otherMatrix = []
    for i in range(0, len(matrix)):
        squareNum = list(map(lambda x: x * x, matrix[i]))
        otherMatrix.append(squareNum)
    return otherMatrix
