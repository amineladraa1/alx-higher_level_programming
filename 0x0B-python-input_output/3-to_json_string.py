#!/usr/bin/python3
"""define a function that returns the JSON representation of object"""
import json

def to_json_string(my_obj):
    """returns a json

        :param my_obj: The object to be serialized.
        :return: A JSON string representing the object.
    """
    return json.dumps(my_obj, sort_keys=True)
