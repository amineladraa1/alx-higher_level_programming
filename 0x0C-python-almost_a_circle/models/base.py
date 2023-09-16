#!/usr/bin/python3
"""define a base class"""
import json

class Base:
    """represents a base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + ".json","w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                l_dict = [obj.to_dictionary() for obj in list_objs]
            f.write(cls.to_json_string(l_dict))

