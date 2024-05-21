#!/usr/bin/python3
"""
This module contains 0 methods and 1 class 'BaseGeometry'
"""


class BaseGeometry():
    """
    This class contains 1 custom method:
        - 'area()'
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("[TypeError] {} must be an integer".format(name))
        if value <= 0:
            raise ValueError("\
                    [ValueError] {} must be greater than 0".format(name))
