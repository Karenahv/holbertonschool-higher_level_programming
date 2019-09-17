#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    if my_list[0] > my_list[1]:
        maximo = my_list[0]
    else:
        maximo = my_list[1]
    for i in range(2, len(my_list)):
        if my_list[i] > maximo:
            maximo = my_list[i]
    return (maximo)
