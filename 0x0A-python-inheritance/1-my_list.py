#!/usr/bin/python3

""" Defines the MyList class """


class MyList(list):
    """ Subclass of list"""
    def __init__(self):
        """Initialize the object"""
        super().__init__()

    def print_sorted(self):
        """Print the sorted list"""
        print(sorted(self))
