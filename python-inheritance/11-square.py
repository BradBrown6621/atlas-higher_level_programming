#!/usr/bin/python3
"""
This module contains 1 class:
    - 'Square(Rectangle)'
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class defines a Square in memory.
    This class contains 1 custom method:
        - '__init__()'
    """

    def __init__(self, size):
        try:
            self.integer_validator("size", size)
        except Exception as e:
            raise e
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
