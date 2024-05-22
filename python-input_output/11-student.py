#!/usr/bin/python3
"""
This module defines 1 custom class:
    - 'Student()'
"""


import json as JSON


class Student():
    """
    This class defines a Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Called when we initialize new Student instances.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This method gives us a dictionary representation a
        Student's attributes.
        """
        if attrs is None:
            return self.__dict__
        return {key: value
                for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """
        This method loads from a JSON file and replaces
        all current attribute values with the ones from the
        JSON file
        """

        self.__dict__ = json
