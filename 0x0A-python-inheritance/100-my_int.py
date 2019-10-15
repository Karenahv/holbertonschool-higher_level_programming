#!/usr/bin/python3
""" class MyInt"""


class MyInt(int):
    """ class MyInt"""
    def __init__(self, integer):
        self.integer = integer

    def __eq__(self, other):
        return self.integer != other

    def __ne__(self, other):
        return self.integer == other
