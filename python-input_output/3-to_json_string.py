#!/usr/bin/python3
"""
This module contains 1 custom method:
    - 'to_json_string(my_obj)'
"""


import json


def to_json_string(my_obj):
    """
    Gives a JSON representation of object 'my_obj'
    """

    return json.dumps(my_obj)
