#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for n in my_list:
        new.append(n)

    for i in new:
        if i == search:
            idx = new.index(i)
            new[idx] = replace
    return new
