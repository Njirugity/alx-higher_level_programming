#!/usr/bin/python3

"""Defines a class Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines rectangle from the BaseGeometry class"""

    def __init__(self, width, height):
        """Initialize instance"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return  a printable string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
