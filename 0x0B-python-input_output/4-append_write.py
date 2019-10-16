#!/usr/bin/python3
""" write a file"""


def append_write(filename="", text=""):
    n = 0
    with open(filename, mode="a", encoding="utf-8") as f:
        n = f.write(text)
    return (n)
