#!/usr/bin/python3
"""
Function that appends a string at the end of a
textfile and returns the number of chars added
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
