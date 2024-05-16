#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return [replace if search is item else item for item in my_list]
