#!/usr/bin/python3
def safe_print_division(a, b):
    division = 0
    try:
        division = a/b
        return division
    except ZeroDivisionError:
        division = None
        return division
    finally:
        print("Inside result: {}".format(division))
