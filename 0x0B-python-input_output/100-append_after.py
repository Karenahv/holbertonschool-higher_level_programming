#!/usr/bin/python3
""" inssert in an specific line"""


def append_after(filename="", search_string="", new_string=""):
    numoflines = 0
    list1 = []
    indices = []
    flag = 0
    with open(filename, encoding="utf-8") as f:
        contenido = f.readlines()
        f.seek(0)
        while True:
            line = f.readline()
            if not line:
                break
            numoflines += 1
            list1 = line.split()
            for word in list1:
                if search_string in word:
                    if flag == 0:
                        contenido.insert(numoflines, new_string)
                        flag = 1
                    else:
                        contenido.insert(numoflines + 1, new_string)
    with open(filename, mode="w", encoding="utf-8") as f:
        contenido = "".join(contenido)
        f.write(contenido)
