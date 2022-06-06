#!/usr/bin/python3
"""Defines unittests for base.py"""
import unittest
import os
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """ Class made to test Base Class """
    def test_pep8_base(self):
        """ Check if pep8 is correct """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_id_as_positive(self):
        """ Test for a positive Base Class id """
        base_instance = Base(18)
        self.assertEqual(base_instance.id, 18)
        base_instance = Base(72)
        self.assertEqual(base_instance.id, 72)
        base_instance = Base(189)
        self.assertEqual(base_instance.id, 189)

    def test_id_as_negative(self):
        """ Test for a negative Base Class id """
        base_instance = Base(-9)
        self.assertEqual(base_instance.id, -9)
        base_instance = Base(-44)
        self.assertEqual(base_instance.id, -44)
        base_instance = Base(-130)
        self.assertEqual(base_instance.id, -130)