#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return None
    return (set(set(set_1).intersection(set_2)))
