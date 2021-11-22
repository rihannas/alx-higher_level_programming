#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in (len(matrix)):
        for column in (len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if column != (len(matrix[i]) - 1):
                print(" ", end="")
        print()
