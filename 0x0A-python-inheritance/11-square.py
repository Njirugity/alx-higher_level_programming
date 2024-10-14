#!/usr/bin/python3

""" Define a class square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Represents a square using Rectangle"""
    
    def __init__(self, size):
        """Initializes instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Return the area"""
        return super().area()

    def __str__(self):
       """Return a printable string"""
       return "[Square] {:d}/{:d}".format(self.__size, self.__size)
