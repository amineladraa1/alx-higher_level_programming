#!/usr/bin/python3
"""defines a function inspects obj instance"""


def is_kind_of_class(obj, a_class):
    """check if in a obj is instance.

    Args:
        obj: object
        a_class: class.
    Returns:
        true if it is an instance
        false if it's not
    """
    if isinstance(obj, a_class):
        return True
    return False
