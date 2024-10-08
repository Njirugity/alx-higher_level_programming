#!/usr/bin/python3
"""Defines an addition function for integers"""


def add_integer(a, b=98):
    """Adds two integers.
    Arg:
        a: First ineger
        b: Second integer
    Return:
        Addition of two numbers
    Raises:
    TypeError: If the arguments are not integers or floats
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
