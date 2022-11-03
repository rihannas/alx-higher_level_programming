#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    # new
    dic = a_dictionary.copy()
    for key, value in dic.items():
        value = value * 2
        dic[key] = value
    return dic

    # old
    # new = {}
    # for i in a_dictionary:
    #     new[i] = a_dictionary[i] * 2
    # return new
