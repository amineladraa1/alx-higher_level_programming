#!/usr/bin/python3
import json as j
"""define a function that returns the JSON representation of object"""


def to_json_string(my_obj):
    """returns a json"""
    return j.dumps(my_obj, sort_keys=True)
