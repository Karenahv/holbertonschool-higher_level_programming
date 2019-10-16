#!/usr/bin/python3
""" write a file"""


def write_file(filename="", text=""):
    n = 0
    with open(filename, mode="w", encoding="utf-8") as f:
        n = f.write(text)
    return (n)
