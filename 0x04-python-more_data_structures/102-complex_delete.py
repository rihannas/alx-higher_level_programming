#!/usr/bin/python3


def complex_delete(a_dictionary, value):

    if value not in a_dictionary.values():
        return a_dictionary

    for k in list(a_dictionary.keys()):
        if a_dictionary.get(k) == value:
            del a_dictionary[k]

    return a_dictionary

    # we need to change a_dictionary.keys() to a-
    # list b/c we get a runtime error if we try to-
    # iterate through a dictionary that changes sizes
