#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in matrix:
            print("{:d}".format(col), end=" " if i != j[-1] else "")
        print()
