#!/usr/bin/python3
"""define a func to add attribute"""


def add_attr(obj, attr, value):
    """check if it has dict before setting new attr
 
    Args:
        obj: object
        attr: new atrribute
        value: of attribute
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
