#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 or tuple_a[0] is None:
        num1 = 0
    else:
        num1 = tuple_a[0]
    if len(tuple_b) == 0 or tuple_b[0] is None:
        num2 = 0
    else:
        num2 = tuple_b[0]
    if len(tuple_a) < 2 or tuple_a[1] is None:
        num3 = 0
    else:
        num3 = tuple_a[1]
    if len(tuple_b) < 2 or tuple_b[1] is None:
        num4 = 0
    else:
        num4 = tuple_b[1]
    sum1 = num1 + num2
    sum2 = num3 + num4
    return (sum1, sum2)
