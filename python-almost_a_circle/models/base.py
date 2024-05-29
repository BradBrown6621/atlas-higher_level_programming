#!/usr/bin/python3
"""
This module contains 1 custom class:
    - 'Base'
"""


import json


class Base():
    """
    This class is a Base class for our geometries
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This function defines a class constructor
        """

        if (id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """
        Gives a JSON representation of list 'list_dictionaries'
        """

        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of the JSON representation of 'json_string'
        """

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method writes a JSON representation of list 'list_objs'
        to a file
        """

        json_list = []
        if list_objs:
            for i in list_objs:
                json_list.append(i.to_dictionary())

        with open(cls.__name__ + ".json", "w") as json_file:
            json_file.write(cls.to_json_string(json_list))

    @classmethod
    def create(cls, **dictionary):
        """
        Creates new instances of classes from dictionary representations
        """

        instance = cls(1, 1)
        instance.update(**dictionary)

        return instance
