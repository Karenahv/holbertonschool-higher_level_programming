#!/usr/bin/python3
"""class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        dic1 = {}
        if hasattr(self, '__dict__'):
            return self.__dict__
        return dic1
