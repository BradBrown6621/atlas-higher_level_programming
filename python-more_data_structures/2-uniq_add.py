#!/usr/bin/python3

def uniq_add(my_list=[]):
    list_uniq = []
    sum_n = 0
    for n in my_list:
        if n not in list_uniq:
            sum_n += n
            list_uniq.append(n)
    return sum_n
