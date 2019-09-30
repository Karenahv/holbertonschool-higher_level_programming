#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
    except IndexError:
        print()
        return i
    print()
    return x
