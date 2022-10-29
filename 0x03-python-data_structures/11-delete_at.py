#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    # new
    idxRange = len(my_list) - 1
    if idx < 0 or idx > idxRange:
        return my_list
    new = my_list.copy()
    my_list.clear()
    for num in new:
        if num != new[idx]:
            my_list.append(num)
    return my_list

    # old
    # element = len(my_list)
    # if idx < 0:
    #     return my_list
    # elif idx > (element - 1):
    #     return my_list
    # else:
    #     del my_list[idx]
    # return my_list
