#!/usr/bin/python3
"""Defines unittests for base.py."""
import unittest
import os
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """
    A class to test the Base Class
    """
    def test_pep8_base(self):
        """
        Test that checks PEP8 pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_id_as_positive(self):
        """
        Test for a positive Base Class id
        """
        base_instance = Base(115)
        self.assertEqual(base_instance.id, 115)
        base_instance = Base(67)
        self.assertEqual(base_instance.id, 67)

    def test_id_as_negative(self):
        """
        Test for a negative Base Class id
        """
        base_instance = Base(-91)
        self.assertEqual(base_instance.id, -91)
        base_instance = Base(-4)
        self.assertEqual(base_instance.id, -4)

    def test_string_id(self):
        """
        Test for a string Base Class id
        """
        base_instance = Base('Hello World')
        self.assertEqual(base_instance.id, 'Hello World')
        base_instance = Base('How are you')
        self.assertEqual(base_instance.id, 'How are you')

    def test_to_json_string(self):
        """
        Test if the to_json_string method works
        """
        json_string = Base.to_json_string([{'value': 1}])
        json_string_two = Base.to_json_string([{'value': 1}, {'value2': 2}])
        self.assertEqual(json_string, '[{"value": 1}]')
        self.assertEqual(json_string_two, '[{"value": 1}, {"value2": 2}]')

    def test_to_json_string_none(self):
        """
        Test when None is passed to to_json_string
        """
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_to_json_string_empty_list(self):
        """
        Test when: to_json_string is passed as an empty list
        """
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, '[]')

    def test_from_empty_json_string(self):
        """
        Test from empty JSON to string (py dict)
        """
        s1 = ""
        strs = Base.from_json_string(s1)
        self.assertTrue(type(strs) == list)
        self.assertTrue(strs == [])

    def test_from_none_to_json_string(self):
        """
        Test fomr None to JSON string (mTy py dict)
        """
        s1 = None
        strs = Base.from_json_string(s1)
        self.assertTrue(type(strs) == list)
        self.assertTrue(strs == [])
