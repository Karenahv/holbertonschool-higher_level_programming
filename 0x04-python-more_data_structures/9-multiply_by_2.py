#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return
    n_dictionary = {}
    for k, v in a_dictionary.items():
        n_dictionary[k] = v * 2
    return n_dictionary
