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
