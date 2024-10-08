#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    msg_for_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_for_size = "Each row of the matrix must have the same size"
    len_e = 0

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_for_type)

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_for_type)

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(msg_for_size)

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msg_for_type)

        len_e = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
    if not isinsatance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

