#!/usr/bin/python3
""" Module MyList that inherits from list """


class MyList(list):
    """ MyList class is a sublcass of list """

    def print_sorted(self):
        """ Print the list in sorted ascending order """
        print(sorted(self))
