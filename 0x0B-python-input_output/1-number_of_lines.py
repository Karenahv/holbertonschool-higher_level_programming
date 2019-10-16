#!/usr/bin/python3
""" counting number of lines in a File"""


def number_of_lines(filename=""):
    with open(filename, encoding="utf-8") as f:
        numlines = 0
        while True:
            line = f.readline()
            if not line:
                break
            numlines += 1

    return (numlines)
