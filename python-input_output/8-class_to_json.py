#!/usr/bin/python3
"""
This module contains 1 custom method:
    - 'class_to_json(obj)'
"""


def class_to_json(obj):
    """
    This method returns the attributes of an object
    in dictionary for (for later JSON serialization)
    """

    return obj.__dict__
