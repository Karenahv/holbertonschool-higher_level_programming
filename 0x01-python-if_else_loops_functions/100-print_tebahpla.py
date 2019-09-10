#!/usr/bin/python3
for i in range(122, 96, -1):
    c = i
    if i % 2 != 0:
        c = i - 32
    print("{}".format(chr(c)), end="")
