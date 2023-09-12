#!/usr/bin/python3
"""define  function that returns the dictionary description"""


def class_to_json(obj):
    """return a dict

    args:
        obj: object
    """
    my_dict = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, int, bool, str)):
            my_dict[key] = value

    return my_dict
