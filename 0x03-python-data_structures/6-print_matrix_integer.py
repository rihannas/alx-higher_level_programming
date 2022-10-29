#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for n in list:
            print("{:d} ".format(n), end="")
        print()
