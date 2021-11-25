#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list == None:
        return None
    else:
        new = my_list.copy()
        for i in my_list:
            if i == search:
                new.append(replace)
        return new
