#!/usr/bin/python3
""" Checks if classes are the same """

def is_same_class(obj, a_class):
	""" Checks if an object is an instance of certain class """
	if type(obj) == a_class:
		return True
	return False
