#!/usr/bin/python3
""" Define class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializates Square """
        super().__init__(size, size, x, y, id)