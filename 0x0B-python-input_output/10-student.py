#!/usr/bin/python3
"""
Define a class Student that defines itself
by first and last name and age
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            new_dict = {}
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        else:
           return self.__dict__
