#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    start = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i], end=""))
            start = 1 + start
        except IndexError:
            break

    print()
    return start
