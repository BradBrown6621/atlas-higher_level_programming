#!/usr/bin/python3
"""
This module contains a single Square class
"""


class Square:
    """
    Square: A class defining a Square
    """
    def real_number_validator(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        return value

    def __init__(self, size=0, position=(0, 0)):
        """
        Creates attribute(s) on instantiation
        """
        try:
            self.real_number_validator(size)
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        try:
            self.real_number_validator(position[0])
            self.real_number_validator(position[1])
            self.__position = position
        except TypeError:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            self.real_number_validator(value)
            self.__size = value
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            self.real_number_validator(value[0])
            self.real_number_validator(value[1])
            self.__position = value
        except TypeError:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print("")
        for p in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for p in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
