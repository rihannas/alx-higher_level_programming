#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    # new
    for row in matrix:
        for column in row:
            print('{:d}'.format(column), end=" ")
        print()

    # old
    # for i in matrix:
    #     for j in i:
    #         if j != i[-1]:
    #             print("{:d}".format(j), end=" ")
    #         else:
    #             print("{:d}".format(j), end="")
    #     print()
