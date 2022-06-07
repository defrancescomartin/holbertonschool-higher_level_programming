#!/usr/bin/python3
"""Defines unittests for rectangle.py."""
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    A class to test the Rectangle Class
    """
    def test_pep8_base(self):
        """
        Test that checks PEP8 pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/rectangle.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_rectangle_subclass(self):
        """
        Test if Rectangle class inherit from
        Base class
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        """
        Test parameters for Rectangle class
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 3)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
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
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def test_string(self):
        """
        Test string parameters for a
        Rectangle class
        """
        with self.assertRaises(TypeError):
            Rectangle('Monty', 'Python')

    def test_width(self):
        """
        Test setting attribute width
        """
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r2.width, 3)

    def test_height(self):
        """
        Test setting attribute height
        """
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)

        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 4)

    def test_no_arguments(self):
        """
        Test when attributes width and height aren't passed
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_with_width_and_height(self):
        """
        Test when attributes width and height are passed
        """
        Base._Base__nb_objects = 0

        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_type_param(self):
        """
        Test different types of parameters
        for a Rectangle class
        """
        with self.assertRaises(TypeError):
            Rectangle(1.01, 3)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(-234234242, 45)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle('', 4)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(True, 4)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 1.76)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, "Hello")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, -4798576398576)
            raise ValueError

        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1.50)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 6, "test")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 7, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, 7, -4798576398576)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1, 1.53)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 6, 5, "test")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 7, 7, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, 9, 5, -4798576398576)
            raise ValueError()