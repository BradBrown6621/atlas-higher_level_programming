#!/usr/bin/python3
"""
This module contains 1 custom method
    - 'read_file(filename="")
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())
