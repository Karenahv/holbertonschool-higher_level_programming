#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) <= 0:
        return None
    maximo = list(a_dictionary.values())[0]
    llave = list(a_dictionary.keys())[0]
    for k, v in a_dictionary.items():
        if v > maximo:
            maximo = v
            llave = k
    return (llave)
