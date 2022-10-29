#!/usr/bin/python3
def max_integer(my_list=[]):
    # new
    if len(my_list) == 0:
        return None
    else:
        my_list.sort()
        return my_list[-1]

    # old
    # if len(my_list) == 0:
    #     return None
    # else:
    #     maxx = my_list[0]
    #     for i in my_list:
    #         if i > maxx:
    #             maxx = i
    #     return maxx
