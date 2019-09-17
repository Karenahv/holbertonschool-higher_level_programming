#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    sizeoflist = len(my_list)
    if idx > sizeoflist - 1 or idx is None or idx < 0 or my_list is None:
        return (my_list)
    my_list[idx] = element
    return (my_list)
