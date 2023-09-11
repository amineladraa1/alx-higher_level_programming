#!/usr/bin/python3
"""defines list class MyList."""


class MyList(list):
    """sorts a list."""

    def print_sorted(self):
        """Print a list."""
        print(sorted(self))
