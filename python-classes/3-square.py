#!/usr/bin/python3
"""
This module contains a single Square class
"""


class Square:
    """
    Square: A class defining a Square
    """
    def __init__(self, size=0):
        """
        Creates attribute(s) on instantiation
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
