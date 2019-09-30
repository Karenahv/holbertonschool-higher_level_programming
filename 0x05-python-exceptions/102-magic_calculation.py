#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                res += a ** b / i
        except:
            res = a + b
            break
    return res
