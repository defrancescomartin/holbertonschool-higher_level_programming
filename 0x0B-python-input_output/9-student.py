#!/usr/bin/python3
"""
Define a class Student that defines itself
by first and last name and age
"""


class Student:
    """ defines a student  """
    def __init__(self, first_name, last_name, age):
    """ initializer  """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
    """ dictionary representation of Student """
        return self.__dict__
