#!/usr/bin/python3
""" Define class Rectangle """
from models.base import Base


Class Rectangle(Base):
    """ Define class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize constructor """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y