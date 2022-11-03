#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    max = 0
    values = a_dictionary.values()
    for value in values:

        if value > max:
            max = value
    # key = [k for k, v in a_dictionary.items() if v == max]

    # returning a key froma value
    for key, value in a_dictionary.items():
        if value == max:
            return key
