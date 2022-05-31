#!/usr/bin/python3
"""
Function that returns the number of chars
written into a string on a textfile
"""


def write_file(filename="", text=""):
    """ write a string into a textfile """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
