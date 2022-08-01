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

    def update(self, *args, **kwargs):
        """Update the class Square assignating an argument to each attr"""
        argc = len(args)
        kwargc = len(kwargs)
        attribute_list = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

        if argc > 0:
            for i in range(argc):
                setattr(self, attribute_list[i], args[i])
        elif kwargc > 0:
            for a, b in kwargs.items():
                if a in attribute_list:
                    setattr(self, a, b)

    def to_dictionary(self):
        """Dictionary representation for Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
