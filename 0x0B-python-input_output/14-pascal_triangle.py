#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    list1 = []
    if n <= 0:
        return list1
    for i in range(n):
        list1.append([])
        list1[i].append(1)
        for j in range(1, i):
            list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
        if i != 0:
            list1[i].append(1)
    return list1
