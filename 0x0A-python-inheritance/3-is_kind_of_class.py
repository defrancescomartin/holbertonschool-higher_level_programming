#!/usr/bin/python3
""" Checks if is kind of class """


def is_kind_of_class(obj, a_class):
    """
    Function that checks if the obj is an instance of a
    specified class or if is an instance of a class
    that inherited from the specified class
    """
    if isinstance(obj, a_class):
        return True
    return False
