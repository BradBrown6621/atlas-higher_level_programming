#!/usr/bin/python3
"""
This module contains 1 method that:
    - Determines if an object is an instance of a given class
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is EXACTLY an instance of a given class.
    isinstance(obj, a_class) can return True in cases where 'a_class'
    is a superclass of 'obj', so that's why it isn't used here.
    """
    return type(obj) is a_class
