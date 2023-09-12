#!/usr/bin/python3
"""defines  function that writes an Object to a text file, using a JSON"""
import json


def save_to_json_file(my_obj, filename):
    """saves a json to file

    args:
        my_obj: object to save
        filename: file to save to
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        json.dump(my_obj, f, sort_keys=True)
