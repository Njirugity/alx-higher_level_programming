#!/usr/bin/python3

"""Define class BaseGeometry. """


class BaseGeometry:
    """ Represents base geometry. """

    def area(self):
        """ Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value
        Args:
             name:  a string
             value: an integer
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
