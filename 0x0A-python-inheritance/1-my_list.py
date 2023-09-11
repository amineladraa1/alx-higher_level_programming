#!/usr/bin/python3
"""define a subclass list with a print sorted mehode."""


class MyList(list):
    """sorts a list"""

    def print_sorted(self):
        """return a sorted list"""
        print(sorted(self))
