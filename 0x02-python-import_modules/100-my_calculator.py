#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    numofargs = len(sys.argv)
    listargs = sys.argv
    list1 = ['+', '-', '*', '/']
    list2 = [add, sub, mul, div]
    i = 0
    flag = 0

    if numofargs != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(listargs[1])
    b = int(listargs[3])
    for operator in list1:
        if operator == listargs[2]:
            print("{} {} {} = {}".format(a, list1[i], b, list2[i](a, b)))
            flag = 1
        i = i + 1
    if flag == 0:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
