#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    namesfunc = dir(hidden_4)
    for i in namesfunc:
        if i[:2] != '__':
            print("{}".format(i))
