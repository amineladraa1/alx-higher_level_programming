#!/usr/bin/python3
import json
"""define a function that returns the JSON representation of object"""


def to_json_string(my_obj):
    """returns a json

        :param my_obj: The object to be serialized.
        :return: A JSON string representing the object.
    """
    return json.dumps(my_obj)
