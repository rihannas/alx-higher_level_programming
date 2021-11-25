#!/usr/bin/python3
def uniq_add(my_list=[]):
    plus = set(my_list)
    total = 0
    for i in plus:
        total = total + i
    return total
