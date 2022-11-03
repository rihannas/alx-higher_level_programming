#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary[i]))


# def print_sorted_dictionary(a_dictionary):
#     keys = a_dictionary.keys()
#     keys = list(keys)
#     keys.sort()
#     for key in keys:
#         print("{}: {}".format(key, a_dictionary[key]))
