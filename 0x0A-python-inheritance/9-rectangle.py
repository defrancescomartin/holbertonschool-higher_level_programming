#!/usr/bin/python3
""" Create a class Rectangle that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Class rectangle using BaseGeometry """

    def __init__(self, width, height):
        """Intializes a new Rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Return the area of the Rectangle """
        return self.__width * self.__height

    def __str__(self):
        """Return the representation of a Rectangle as width/height"""
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
