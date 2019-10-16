#!/usr/bin/python3
"""class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dic1 = {}
        dic2 = {}
        if attrs is None:
            return self.__dict__
        totalargs = len(attrs)
        if hasattr(self, '__dict__'):
            dic1 = self.__dict__
            for key, value in dic1.items():
                for i in range(totalargs):
                    if key == attrs[i]:
                        dic2[key] = value
            return dic2
        return dic1
