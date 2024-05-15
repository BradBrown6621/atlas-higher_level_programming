#!/usr/bin/python3

def element_at(my_list, idx):
    if (type(my_list) == list) and (idx >= 0) and (idx <= len(my_list)):
        return (my_list[idx])
    return None
