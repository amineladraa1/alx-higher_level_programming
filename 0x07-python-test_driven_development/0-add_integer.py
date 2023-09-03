#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float are typecasted to ints before addition.

    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number Defaults to 98.

    Returns:
        int: The result of adding a and b as integers.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
