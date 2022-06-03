#!/usr/bin/python3
""" Define class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializates Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a Square into a String representation """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size """
        self.width = value
        self.height = value