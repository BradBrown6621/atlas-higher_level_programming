#!/usr/bin/python3
"""
This module defines 1 class:
    - 'Rectangle(BaseGeometry)'
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class contains 4 custom methods:
        - '__init__(self, width, height)'
        - 'area(self)'
        - 'print(self)'
        - 'str()'
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
            self.__height = height

    def area(self):
        return self.__width * self.__height

    def print(self):
        print(str(self))

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
