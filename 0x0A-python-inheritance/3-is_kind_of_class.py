#!/usr/bin/python3
""" check type object"""


def is_kind_of_class(obj, a_class):
    """ check type object"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
