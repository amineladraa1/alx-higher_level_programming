#!/usr/bin/python3
"""Defines a function."""


def inherits_from(obj, a_class):
    """Checks object inherited instance of a class.

    Args:
        obj : object to check.
        a_class : class.
    Returns:
        True if it is a subclass.
        False if not.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
