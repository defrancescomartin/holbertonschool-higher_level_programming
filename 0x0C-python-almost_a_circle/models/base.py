#!/usr/bin/python3
""" Define class Base """
import json
from os import path


<<<<<<< HEAD
class Base(object):
=======
class Base(object)
>>>>>>> 46c413a9d46b13b1c77b185e82e373d0d708ada9
    """" Define class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects       