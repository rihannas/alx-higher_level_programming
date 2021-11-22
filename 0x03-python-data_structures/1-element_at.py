#!/usr/bin/python3
def element_at(my_list, idx):
    element = len(my_list) - 1
    if idx < 0:
        return None
    elif idx > element:
        return None
    else: 
        return my_list[idx]
