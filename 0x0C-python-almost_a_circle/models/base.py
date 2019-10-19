#!/usr/bin/python3
"""class base"""


import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        string = "[]"
        if list_dictionaries is None:
            return string
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))
