#!/usr/bin/python3

def no_c(my_string):
    noC = ''
    for n in (my_string):
        if n != "c" and n != "C":
            noC = noC + n  # concatenation :)

    return noC
