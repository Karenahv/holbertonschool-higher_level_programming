#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    sizeoflist = len(my_list)
    if idx > sizeoflist - 1:
        return (my_list)
    if idx > 0:
        my_list[idx] = element
        return (my_list)
    return (my_list)
