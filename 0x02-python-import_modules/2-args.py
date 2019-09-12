#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numofargs = len(sys.argv)
    listargs = sys.argv
    if numofargs == 1:
        print("{} arguments.".format(numofargs - 1))
    elif numofargs == 2:
        print("{} argument:".format(numofargs - 1))
        print("{}: {}".format(1, listargs[1]))
    else:
        print("{} arguments:".format(numofargs - 1))
        for i in range(1, numofargs):
            print("{}: {}".format(i, listargs[i]))
