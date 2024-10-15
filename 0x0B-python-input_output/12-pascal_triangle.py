#!/usr/bin/python3

def pascal_triangle(n):
    """ Function that returns the pascal triangle
    Args:
        n: number of lines
    Returns:
        matrix: a matrix with the pascal triangle
    """

    triangle = []
    temp = []

    for i in range(n):
        new = []
        idx1 = -1
        idx2 = 0
        for j in range(len(temp) + 1):
            if idx1 == -1 or idx2 == len(temp):
                new += [1]
            else:
                new += [new[idx1] + new[idx2]]
            idx1 += 1
            idx2 += 1

        triangle.append(new)
        temp = new[:]

    return triangle
