#!/usr/bin/python3


"""
a function that returns the weighted average of all
integers tuple (<score>, <weight>)
"""


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    prodList = []
    sumDom = 0
    for tple in my_list:
        sumDom = sumDom + tple[1]
        product = tple[0] * tple[1]
        prodList.append(product)
        product = 0

    sum = 0
    for n in prodList:
        sum = sum + n

    average = sum/sumDom
    return average
