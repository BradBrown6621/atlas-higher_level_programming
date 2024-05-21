#!/usr/bin/python3
"""
This module defines 1 custom method:
    - 'load_from_json_file(filename)'
"""


import json


def load_from_json_file(filename):
    """
    This method deserializes json strings in files
    into Python objects
    """

    with open(filename, mode="r", encoding="utf-8") as json_file:
        return json.loads(json_file.read())
