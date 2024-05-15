#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if (type(my_list) is list) and (idx >= 0) and (idx < len(my_list)):
        new = my_list.copy()
        new[idx] = element
        return new
    return my_list
