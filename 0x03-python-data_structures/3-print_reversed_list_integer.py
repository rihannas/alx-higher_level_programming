#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    revList = reverse(my_list)
    for i in revList:
        print("{:d}".format(i))
