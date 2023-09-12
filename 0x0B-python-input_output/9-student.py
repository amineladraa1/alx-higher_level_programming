#!/usr/bin/python3
"""define a student class"""


class Student:
    """student represntation"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        my_dict = {}

        for key, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                my_dict[key] = value

        return my_dict
