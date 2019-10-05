#!/usr/bin/python3
""" multiply"""


def matrix_mul(m_a, m_b):
    """ multiply"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if isinstance(m_a[0], list) is False:
        raise TypeError("m_a must be a list of lists")
    if isinstance(m_b[0], list) is False:
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    lenmatrixa = len(m_a)
    lenrowa = len(m_a[0])
    lenmatrixb = len(m_b)
    lenrowb = len(m_b[0])
    for i in range(lenmatrixa):
        if len(m_a[i]) != lenrowa:
            raise TypeError("each row of m_a must be of the same size")
    for i in range(lenmatrixb):
        if len(m_b[i]) != lenrowb:
            raise TypeError("each row of m_b must be of the same size")
    for i in range(lenmatrixa):
        for j in range(lenrowa):
            if type(m_a[i][j]) is not int and type(m_a[i][j]) is not\
               float:
                raise TypeError("m_a should contain only integers or floats")
    for i in range(lenmatrixb):
        for j in range(lenrowb):
            if type(m_b[i][j]) is not int and type(m_b[i][j]) is not\
               float:
                raise TypeError("m_b should contain only integers or floats")
    if lenrowa != lenmatrixb:
        raise IndexError("m_a and m_b can't be multiplied")
    matrix = []
    result = 0
    for i in range(lenmatrixa):
        row = []
        for j in range(lenrowb):
            result = 0
            for k in range(lenrowa):
                result += m_a[i][k] * m_b[k][j]
            row.append(result)
        matrix.append(row)
    return matrix
