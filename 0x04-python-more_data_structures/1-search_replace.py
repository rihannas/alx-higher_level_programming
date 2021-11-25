#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list == None:
        return None
    new = my_list.copy()
    for i in new:
        if i == search:
            x = newList.index(i)
            new[x] = replace
    return new
