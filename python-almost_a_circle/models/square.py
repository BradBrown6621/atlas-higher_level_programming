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

    @property
    def size(self):
        """
        Getter for Square.__width
        """

        return self.width

    @size.setter
    def size(self, size):
        """
        Setter for Square.__width
        """

        self.width = size
        self.height = size

    def __str__(self):
        """
        String representation of a 'Square' instance
        """

        return "[Square] ({}) {}/{} - {}".format(
                                                self.id,
                                                self.x,
                                                self.y,
                                                self.size
                                                )

    def update(self, *args, **kwargs):
        """
        Updates 'Square' instance attributes
        """
        if args is not None and len(args) != 0:
            attributes = [
                    'id',
                    'width',
                    'x',
                    'y'
                    ]
            for i in range(len(attributes)):
                if i < len(args):
                    setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary respresentation of class instance 'Square'
        """

        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'size': self.size
                }
