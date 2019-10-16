#!/usr/bin/python3
""" write a json file"""


import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
