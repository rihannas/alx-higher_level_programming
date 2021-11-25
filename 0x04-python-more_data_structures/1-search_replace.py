#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for i in range(new):
        if i == search:
            new.append(replace)
        else:
            new.append(i)
    return new
