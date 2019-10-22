#!/usr/bin/python3
"""class base"""


import json
import csv


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class base"""
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
                    json_string = cls.to_json_string([ob.to_dictionary()
                                                     for ob in list_objs])
                    f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        empty_list = []
        if json_string is None:
            return (empty_list)
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            r10 = Rectangle(1, 1)
        elif cls is Square:
            r10 = Square(1)
        else:
            r10 = None
        r10.update(**dictionary)
        return (r10)

    @classmethod
    def load_from_file(cls):
        import os.path
        filename = cls.__name__ + '.json'
        list1 = []
        if os.path.isfile(filename):
            with open(filename, mode="r", encoding="utf-8") as f:
                json_string = f.read()
                return [cls.create(**dictionary) for dictionary in
                        cls.from_json_string(json_string)]
        else:
            return (list1)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + '.csv'
        csv_todict = [o.to_dictionary() for o in list_objs]
        with open(filename, mode="w", encoding="utf-8") as f:
            dwriter = csv.DictWriter(f, csv_todict[0].keys())
            dwriter.writeheader()
            dwriter.writerows(csv_todict)

    @classmethod
    def load_from_file_csv(cls):
        obj_list = []
        filename = cls.__name__ + '.csv'
        with open(filename, mode="r", encoding="utf-8") as f:
            dreader = csv.DictReader(f)
            for row in dreader:
                t = {}
                for key, value in dict(row).items():
                    t[key] = int(value)
                obj_list.append(cls.create(**t))
        return(obj_list)
