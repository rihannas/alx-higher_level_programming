#!/usr/bin/python3
"""Module to create a Pascal triangle"""


def pascal_triangle(n: int):
    """returns a pascal triangle"""
    res = [[1]]
    for i in range(n - 1):
        template = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            value = template[j] + template[j + 1]
            row.append(value)
        res.append(row)

    return res
