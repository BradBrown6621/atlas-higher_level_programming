#!/usr/bin/python3
"""
This module contains 1 custom method:
    - 'from_json_string(my_str)'
"""


import json


def from_json_string(my_str):
    """
    This method deserializes JSON strings as Python objects.
    """

    return json.loads(my_str)
