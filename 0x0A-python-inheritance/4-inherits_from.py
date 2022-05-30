#!/usr/bin/python3
"""
Function that checks if the object is an instance
of a class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """
    Function that checks if the object is a class
    or inherited class of a_class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
