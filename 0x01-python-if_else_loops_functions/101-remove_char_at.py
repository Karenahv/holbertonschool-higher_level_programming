#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    for i in range(len(str)):
        if i != n:
            str2 += str[i]
    return(str2)
