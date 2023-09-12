#!/usr/bin/python3
""" class Student that defines a student"""


class Student:
    """student instance"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list of str, optional): A list of attributes
                If None, retrieve all attributes.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        my_dict = {}

        if attrs is None:
            for key, value in self.__dict__.items():
                if isinstance(value, (list, dict, str, int, bool)):
                    my_dict[key] = value
        else:
            for at in attrs:
                if hasattr(self, at):
                    value = getattr(self, at)
                    if isinstance(value, (list, dict, str, int, bool)):
                        my_dict[at] = value

        return my_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a dict.

        Args:
            json (dict): A dictionary with attribute names as keys.
        """
        for key, value in json.items():
            setattr(self, key, value)
