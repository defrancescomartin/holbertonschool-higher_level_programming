#!/usr/bin/python3
""" Define class Base """
import json
from os import path


class Base(object)
    """" Define class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects       