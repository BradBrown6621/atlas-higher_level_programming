#!/usr/bin/python3
"""
This module defines 1 custom class:
    - 'Student()'
"""


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

    def to_json(self):
        """
        This method gives us a dictionary representation a
        Student's attributes.
        """

        return self.__dict__
