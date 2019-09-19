#!/usr/bin/python3
def equivalence(roman_letter):
    if (roman_letter == 'I'):
        return 1
    if (roman_letter == 'V'):
        return 5
    if (roman_letter == 'X'):
        return 10
    if (roman_letter == 'L'):
        return 50
    if (roman_letter == 'C'):
        return 100
    if (roman_letter == 'D'):
        return 500
    if (roman_letter == 'M'):
        return 1000
    return -1


def roman_to_int(roman_string):
    resultado = 0
    i = 0
    if roman_string is None or type(roman_string) is not str:
        return 0
    while i < len(roman_string):
        s1 = equivalence(roman_string[i])
        if (i + 1 < len(roman_string)):
            s2 = equivalence(roman_string[i + 1])
            if (s1 >= s2):
                resultado = resultado + s1
                i = i + 1
            else:
                resultado = resultado + s2 - s1
                i = i + 2
        else:
            resultado = resultado + s1
            i = i + 1
    return (resultado)
