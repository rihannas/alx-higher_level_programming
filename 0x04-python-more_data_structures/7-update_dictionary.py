#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key is in a_dictionary:
        for key in a_dictionary:
            a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary[key]
