#!/usr/bin/python3
"""add attribute"""


def add_attribute(ob, name, value):
    if hasattr(ob, '__dict__'):
        setattr(ob, name, value)
    else:
        raise TypeError("can't add new attribute")
