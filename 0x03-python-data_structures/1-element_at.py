#!/usr/bin/python3
def element_at(my_list, idx):
    sizeoflist = len(my_list)
    if idx > sizeoflist - 1 or idx < 0 or my_list is None or idx is None:
        return
    return (my_list[idx])
