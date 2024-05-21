#!/usr/bin/python3
"""
This module contains 1 method:
    -   'inherits_from()'
"""


def inherits_from(obj, a_class):
    """
    This method checks if object 'obj' inherits from class 'a_class'.
    Note that if the type of 'obj' is exactly 'a_class' then 'obj'
    doesn't inherit from 'a_class'
    """

    return (type(obj) is not a_class and isinstance(obj, a_class))
