#!/usr/bin/python3

def best_score(a_dictionary):
    if (a_dictionary is not None) and (len(a_dictionary) > 0):
        for key, value in a_dictionary.items():
            if value == max(a_dictionary.values()):
                return key
