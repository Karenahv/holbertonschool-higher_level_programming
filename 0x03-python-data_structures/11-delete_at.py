#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    sizeoflist = len(my_list)
    if idx > sizeoflist - 1 or idx < 0 or my_list is None or idx is None:
        return (my_list)
    del my_list[idx]
    return (my_list)
