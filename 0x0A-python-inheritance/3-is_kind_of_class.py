#!/usr/bin/python3

""" Defines function that checks if the object is an instance
    or if the object is an instance of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
