#!/usr/bin/python3

""" Define a operator invertor. """


class MyInt(int):
    """Represents a rebel that inverts the == and != operators"""

    def __eq__(self, x):
        """ Overides the == operator."""
        return int.__ne__(self, x)

    def __ne__(self, x):
        """Overides the != operator."""
        return int.__eq__(self, x)
