#!/usr/bin/python3
"""
This module contains 1 custom class:
    -   'Square'
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class contains a to-be-determined amount of methods
    -   List methods here
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square
        """

        super().__init__(size, size, x, y, id)
