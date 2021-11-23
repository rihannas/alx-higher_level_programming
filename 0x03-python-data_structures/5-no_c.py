#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    i = 0
    for i in my_string:
        if my_string[i] != char(99) or my_string[i] != char(67):
            new_string = new_string + my_string[i]
    return new_string
