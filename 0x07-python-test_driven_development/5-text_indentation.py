#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == '.':
            print('.')
            print()
        elif text[i] == '?':
            print('?')
            print()
        elif text[i] == ':':
            print(':')
            print()
        else:
            if (text[i] == ' ' and (text[i - 1]
                                    in ".?:" or text[i - 1] == ' ')):
                continue
            print("{}".format(text[i]), end="")
