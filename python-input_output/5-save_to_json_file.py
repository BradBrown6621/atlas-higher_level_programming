#!/usr/bin/python3
"""
This module contains 1 custom method:
    - 'save_to_json_file(my_obj, filename)'
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This method saves an object 'my_obj' to a text file 'filename'
    """

    with open(filename, mode="w", encoding="utf-8") as my_file:
        my_file.write(json.dumps(my_obj))
