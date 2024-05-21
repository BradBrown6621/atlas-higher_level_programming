#!/usr/bin/python3
"""
This module contains 1 method:
    -   ('is_kind_of_class')
"""


def is_kind_of_class(obj, a_class):
    """
    A method that returns true if 'obj' is an instance
    of 'a_class' or any of it's superclasses.
    """
    return isinstance(obj, a_class)
