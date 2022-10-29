#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    # new
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            tuple_a = tuple_a + (0, )
        elif len(tuple_a) == 0:
            tuple_a = (0, 0)
    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            tuple_b = tuple_b + (0, )
        elif len(tuple_b) == 0:
            tuple_b = (0, 0)

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple

    # old
    # la = len(tuple_a)
    # lb = len(tuple_b)

    # if la < 2 or lb < 2:
    #     tuple_a = tuple_a + (0, 0)
    #     tuple_b = tuple_b + (0, 0)
    # new = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    # return new
