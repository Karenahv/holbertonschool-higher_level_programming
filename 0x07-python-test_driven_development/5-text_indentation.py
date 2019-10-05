#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char == '.':
            print('.')
            print()
        elif char == '?':
            print('?')
            print()
        elif char == ':':
            print(':')
            print()
        else:
            print("{}".format(char), end="")
