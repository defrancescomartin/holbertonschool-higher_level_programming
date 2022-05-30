#!/usr/bin/python3
"""
Create a subclass Square that inherits from class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square - is a subclass of Rectangle
    """
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """override __str__ of Rectangle"""
        return f"[Square] {self.__size}/{self.__size}"
