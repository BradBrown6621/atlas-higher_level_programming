#!/usr/bin/python3
"""
This module contains 1 custom method:
    - 'append_write(filename="", text="")'
"""


def append_write(filename="", text=""):
    """
    This method appends to the end of a file 'filename'
    the data 'text'
    """

    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
