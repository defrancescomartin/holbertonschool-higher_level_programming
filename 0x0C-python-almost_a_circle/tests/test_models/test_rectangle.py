#!/usr/bin/python3
"""Defines unittests for rectangle.py"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Class made to test Rectangle Class """
    def test_pep8_base(self):
        """ Check if pep8 is correct """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_rectangle_subclass(self):
        """ Test if Rectangle Class inherits from Base class"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        """ Test parameters for Rectangle Class """
        r1 = Rectangle(20, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 20, 0, 0, 3)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 20)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def test_string(self):
        """Test string parameters for Rectangle Class """
        with self.assertRaises(TypeError):
            Rectangle('Test', 'string')

    def test_type_param(self):
        """ Test lots of different types of parameters for Rectangle class"""
        with self.assertRaises(TypeError):
            Rectangle(9.01, 2)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(-242, 45)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle('', 8)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(False, 1)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(2, 11.9)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, "Fail")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, False)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 1, "Fail")
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, -476)
            raise ValueError

        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1.50)
            raise TypeError()


        with self.assertRaises(TypeError):
            Rectangle(5, 9, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, 6, -47985)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1, 1.3)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 6, 5, "Fail")
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, 9, 6, -47398576)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle(5, 7, 7, False)
            raise TypeError()
