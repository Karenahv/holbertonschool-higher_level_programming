#!/usr/bin/python3
""" check type object"""


def inherits_from(obj, a_class):
    """ check type object"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
