#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = list(set(my_list))
    total = 0
    for n in my_list:
        total = total + n
    return total

    # new = []
    # for n in my_list:
    #     if n not in new:
    #         new.append(n)
    # lenn = len(new)
    # n = 0
    # for i in range(0, lenn):
    #     n = n + new[i]
    # return n.
