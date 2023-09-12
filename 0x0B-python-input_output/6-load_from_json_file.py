#!/usr/bin/python3
"""defines  function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """create obj from a json to file

    args:
        filename: file to save to
    """
    with open(filename, encoding="UTF-8") as f:
        return json.load(f)

