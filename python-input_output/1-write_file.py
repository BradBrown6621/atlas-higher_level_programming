#!/usr/bin/python3
"""
This module contains 1 custom method:
    - 'write_file(filename="", text="")'
"""


def write_file(filename="", text=""):
    """
    This method writes a string 'text' to a text file 'filename' in UTF8 formatting
    """

    with open(filename, mode="w", encoding="utf-8") as my_file:
        return my_file.write(text)
