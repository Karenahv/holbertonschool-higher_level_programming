#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if i < j:
            if i != 8:
                print("{}{}".format(i, j), end=", ")
            else:
                print("{}{}".format(i, j))
