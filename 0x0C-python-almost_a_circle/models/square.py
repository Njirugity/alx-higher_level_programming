#!/usr/bin/python3
"""Define a rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent the class Square, a subclass of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Intialize an instance
        Args:
        size: The width and height of a square
        x, y: The x and y coordinates of a square respectively
        id: The identification of a square
        """

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Get the size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size of a square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign arguments to attributes"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id == arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                else:
                    continue

        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break

    def to_dictionary(self):
        """Returns the dictionary representaion of Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
