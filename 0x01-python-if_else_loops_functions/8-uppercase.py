#!/usr/bin/python3
"""
a function that prints a string in uppercase followed by a new line.
"""


def uppercase(str):
    for char in str:
        if ord(char) in range(97, 123):
            char = ord(char) - 32
            char = chr(char)
            print('{}'.format(char), end="")
    print()
