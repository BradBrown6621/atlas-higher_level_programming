#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if (type(my_list) is list) and (idx >= 0) and (idx < len(my_list)):
        my_list[idx] = element
    return my_list
