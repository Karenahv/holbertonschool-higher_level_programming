#!/usr/bin/python3
""" reads n lines of a file text"""


def read_lines(filename="", nb_lines=0):
    i = 0
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return
        while i < nb_lines:
            line = f.readline()
            print(line, end="")
            i += 1
