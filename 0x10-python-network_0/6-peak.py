#!/usr/bin/python3
""" a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """finds a peak in list_of_integers."""

    if list_of_integers is None or list_of_integers == []:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)

    mid = len(list_of_integers) // 2

    if len(list_of_integers) != mid + 1:
        if list_of_integers[mid - 1] <= list_of_integers[mid] and \
                list_of_integers[mid + 1] <= list_of_integers[mid]:
            return list_of_integers[mid]
    else:
        if list_of_integers[mid - 1] <= list_of_integers[mid]:
            return list_of_integers[mid]
        else:
            return list_of_integers[mid - 1]

    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    else:
        return find_peak(list_of_integers[:mid])
