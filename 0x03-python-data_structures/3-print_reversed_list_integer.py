#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return None
    if isinstance(my_list, list):
        my_list.reverse()
        for integer in my_list:
            print("{:d}".format(integer))
