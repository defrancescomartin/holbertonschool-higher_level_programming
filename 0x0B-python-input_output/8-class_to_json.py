#!/usr/bin/python3
"""
Function that returns the dictionary desc
with simple data strcuture for JSON serialization
of an object
"""


def class_to_json(obj):
    """ return dictionary description with simple data structure"""
    return obj.__dict__
