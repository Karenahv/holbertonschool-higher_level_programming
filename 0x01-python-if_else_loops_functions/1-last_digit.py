#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
string = "and is less than 6 and not 0"
string2 = "and is greater than 5"
if number >= 0:
    if last_digit > 5:
        print("Last digit of", number, "is", last_digit, string2)
    elif last_digit == 0:
        print("Last digit of", number, "is", last_digit, "and is 0")
    else:
        print("Last digit of", number, "is", last_digit, string)

if number < 0:
    if last_digit != 0:
        print("Last digit of", number, "is", last_digit * -1, string)
    else:
        print("Last digit of", number, "is", last_digit, "and is 0")
