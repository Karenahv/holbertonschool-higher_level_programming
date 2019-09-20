#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    suma = sum(i[0] * i[1] for i in my_list)
    suma2 = sum(j[1] for j in my_list)
    return (suma/suma2)
