#!/usr/bin/python3
"""Defines unittests for square.py"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Class made to test Square Class """
    def test_pep8_base(self):
        """ Check if pep8 is correct """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/square.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_getter(self):
        r1 = Square(2)
        self.assertEqual(r1.size, 2)

    def test_setter(self):
        r1 = Square(2)
        r1.size = 6
        self.assertEqual(r1.size, 6)

    def test_negative(self):
        r1 = Square(4)

        with self.assertRaises(ValueError):
            r1.size = -2

    def test_zero(self):
        r1 = Square(8)

        with self.assertRaises(ValueError):
            r1.size = 0

    def test_width(self):
        r1 = Square(5)
        r1.size = 2
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)

    def test_string(self):
        r1 = Square(9)

        with self.assertRaises(TypeError):
            r1.size = "NaN"

    def test_float(self):
        r1 = Square(4)

        with self.assertRaises(TypeError):
            r1.size = 2.2

    def test_tuple(self):
        r1 = Square(4)

        with self.assertRaises(TypeError):
            r1.size = (6, 9)

    def test_empty(self):
        r1 = Square(7)

        with self.assertRaises(TypeError):
            r1.size = ''

    def test_none(self):
        r1 = Square(8)

        with self.assertRaises(TypeError):
            r1.size = None

    def test_list(self):
        r1 = Square(5)

        with self.assertRaises(TypeError):
            r1.size = [1, 2, 3]

    def test_dict(self):
        r1 = Square(6)

        with self.assertRaises(TypeError):
            r1.size = {"Test": 5, "Failed": 8}
