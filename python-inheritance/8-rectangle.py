#!/usr/bin/python3
"""
This module defines 1 class:
    - 'Rectangle(BaseGeometry)'
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    This class contains 1 custom method:
        - '__init__(self, width, height)'
    """

    def __init__(self, width, height):
        try:
            self.integer_validator("width", width)
        except Exception as e:
            raise e
        else:
            self.__width = width

        try:
            self.integer_validator("height", height)
        except Exception as e:
            raise e
        else:
            self.__width = width
