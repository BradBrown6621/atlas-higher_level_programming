#!/usr/bin/python3
"""
This module contains 1 custom class
-   'Rectangle'
"""

from models.base import Base


class Rectangle(Base):
    """
    This class contains 10 custom methods:
    -   '__init__()'
    -   'width()' (setter and getter)
    -   'height()' (setter and getter)
    -   'x()' (setter and getter)
    -   'y()' (setter and getter)
    -   'integer_validator()'
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This method creates methods of the 'Rectangle' class
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Private attribute '__width' getter
        """

        return self.__width

    @width.setter
    def width(self, width):
        """
        Private attribute '__width' setter
        """

        self.integer_validator("width", width)
        self.__width = width

    @property
    def height(self):
        """
        Private attribute '__height' getter
        """

        return self.__height

    @height.setter
    def height(self, height):
        """
        Private attribute '__height' setter
        """

        self.integer_validator("height", height)
        self.__height = height

    @property
    def x(self):
        """
        Private attribute '__x' getter
        """

        return self.__x

    @x.setter
    def x(self, x):
        """
        Private attribute '__x' setter
        """

        self.integer_validator("x", x)
        self.__x = x

    @property
    def y(self):
        """
        Private attribute '__y' getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Private attribute '__y' setter
        """

        self.integer_validator("y", y)
        self.__y = y

    def integer_validator(self, name, value):
        """
        Checks type/value of integers to make sure we don't
        pass non-integers to places we don't want to
        """

        if type(value) is not int:
            raise TypeError(
                    "{} must be an integer".format(name))
        elif name in ("x", "y"):
            if value < 0:
                raise ValueError(
                        "{} must be >= 0".format(name))
        elif value <= 0:
            raise ValueError(
                    "{} must be > 0".format(name))

    def area(self):
        """
        Gets the area of the rectangle.
        """

        return (self.__width * self.__height)

    def display(self):
        """
        Displays the 'Rectangle' using '#'s
        Example:
            rect = Rectangle(3, 3)
            rect.display()
            -----------
            ###
            ###
            ###
            -----------
        """

        output = ""
        for y in range(0, self.__y):
            output += "\n"
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                output += " "
            for j in range(0, self.__width):
                output += "#"
            output += "\n"
        print(output)
        return output

    def update(self, *args, **kwargs):
        """
        Updates 'Rectangle' instance attributes
        """
        if args is not None and len(args) != 0:
            attributes = [
                    'id',
                    'width',
                    'height',
                    'x',
                    'y'
                    ]
            for i in range(len(attributes)):
                if i < len(args):
                    setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of class instance 'Rectangle'
        in the following format:
        -   '[Rectangle] (<id>) <x>/<y> - <width>/<height>'
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
                    self.id,
                    self.__x,
                    self.__y,
                    self.__width,
                    self.__height
                    )
                )
