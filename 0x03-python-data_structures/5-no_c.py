#!/usr/bin/python3

def no_c(my_string):
    if "c" in my_string:
        noC = my_string.replace("c", "")

    if "C" in my_string:
        noC = my_string.replace("C", "")
    return noC


# def no_c(my_string):
#     new_string = ''
#     for i in (my_string):
#         if i != 'c' and i != 'C':
#             new_string += i
#     return new_string
