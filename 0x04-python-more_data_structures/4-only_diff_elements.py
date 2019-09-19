#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return None
    new_set = list([i for i in set_1 if i not in set_2])
    new_set2 = list([i for i in set_2 if i not in set_1])
    new_set2 = new_set + new_set2
    return (new_set2)
