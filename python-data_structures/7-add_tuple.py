#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_list = [0, 0]
    new_list[0] = \
        (tuple_a[0] if len(tuple_a) > 0 else 0) +\
        (tuple_b[0] if len(tuple_b) > 0 else 0)
    new_list[1] = \
        (tuple_a[1] if len(tuple_a) > 1 else 0) +\
        (tuple_b[1] if len(tuple_b) > 1 else 0)
    return (tuple(new_list))
