#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key is in a_dictionary:
        for i in a_dictionary:
            i = key
            a_dictionary[i] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
