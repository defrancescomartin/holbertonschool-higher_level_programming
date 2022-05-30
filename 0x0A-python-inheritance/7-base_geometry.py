#!/usr/bin/python3
""" Creates an empty class BaseGeometry """


class BaseGeometry:
    """ Class BaseGeometry """

    def area(self):
        """ area function """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validate a parameter as an int """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
