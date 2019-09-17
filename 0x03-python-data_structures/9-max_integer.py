#!/usr/bin/python3
def max_integer(my_list=[]):
    if isinstance(my_list, list):
        if my_list[0] > my_list[1]:
            maximo = my_list[0]
        else:
            maximo = my_list[1]
            for i in range(1, len(my_list)):
                if my_list[i] > maximo:
                    maximo = my_list[i]
        return (maximo)
