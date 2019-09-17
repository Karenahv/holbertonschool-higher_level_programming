#!/usr/bin/env python
def no_c(my_string):
    return (my_string.translate({ord(i): None for i in 'cC'}))
