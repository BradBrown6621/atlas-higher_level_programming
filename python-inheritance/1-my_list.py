#!/usr/bin/python3
"""
This module contains a custom 'MyList()' class
"""


class MyList(list):
    """
    Class that inherits from 'list' class
    """

    def print_sorted(self):
        sorted_self = [i for i in self]
        sorted_self.sort()
        print(sorted_self)
