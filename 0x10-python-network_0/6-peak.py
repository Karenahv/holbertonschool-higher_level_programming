#!/usr/bin/python3
""" find peak"""


def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    if list_of_integers[0] >= list_of_integers[1]:
        return (list_of_integers[0])
    else:
        for i in range(1, len(list_of_integers)):
            try:
                if (list_of_integers[i] >= list_of_integers[i - 1] and
                   list_of_integers[i] >= list_of_integers[i + 1]):
                    return list_of_integers[i]
            except:
                return list_of_integers[len(list_of_integers)]
