#!/usr/bin/python3
""" print squares"""


def print_square(size):
    """ print squares"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
            for j in range(size):
                if j != (size - 1):
                    print("{}". format("#"), end="")
                else:
                    print("#")
