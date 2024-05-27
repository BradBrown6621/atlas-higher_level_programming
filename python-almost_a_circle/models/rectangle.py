#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        attributes = {
                '_Rectangle__width': width,
                '_Rectangle__height': height,
                '_Rectangle__x': x,
                '_Rectangle__y': y
                }
        for name, value in attributes.items():
            try:
                self.integer_validator(name[len("_Rectangle__"):], value)
            except Exception as e:
                print(e)
            else:
                setattr(self, name, value)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        try:
            self.integer_validator("width", width)
        except Exception as e:
            print(e)
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__width = width

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        try:
            self.integer_validator("x", x)
        except Exception as e:
            print(e)
        else:
            self.__x = x

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, y):
        self.__y = y

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(
                    "[TypeError] {} must be an integer".format(name))
        elif name in ("x", "y"):
            if value < 0:
                raise ValueError(
                        "[ValueError] {} must be >= 0".format(name))
        elif value <= 0:
            raise ValueError(
                    "[ValueError] {} must be > 0".format(name))
