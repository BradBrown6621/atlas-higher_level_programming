#!usr/bin/python3
"""
This module contains 1 custom class:
    - 'Base'
"""


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
