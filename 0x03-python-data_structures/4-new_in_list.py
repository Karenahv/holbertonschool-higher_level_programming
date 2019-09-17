#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    sizeoflist = len(my_list)
    if idx > sizeoflist - 1:
        return (my_list)
    if idx > 0:
        new_list[idx] = element
        return (new_list)
    return (my_list)
