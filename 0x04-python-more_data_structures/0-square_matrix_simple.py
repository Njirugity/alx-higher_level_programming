#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for n in matrix:
        square = list(map(lambda x: x**2, n))
        newMatrix.append(square)
    return newMatrix
