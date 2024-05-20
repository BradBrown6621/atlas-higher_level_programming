#!/usr/bin/python3

def add_integer(a, b=98):
    try:
        if not isinstance(a, int) and not isinstance(a, float):
            raise TypeError
    except TypeError:
        raise TypeError("a must be an integer")
    else:
        try:
            if not isinstance(b, int) and not isinstance(b, float):
                raise TypeError
        except TypeError:
            raise TypeError("b must be an integer")
        else:
            return int(a) + int(b)
