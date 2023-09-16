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

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
    @classmethod
    def load_from_file(cls):
        try:
            with open(str(cls.__name__) + ".json", "r") as f:
                li_dicts = cls.from_json_string(f.read())
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []
