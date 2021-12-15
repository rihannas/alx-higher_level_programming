#!/usr/bin/python3
"""
Module text_indentation
Adds to lines after . : ?
"""


def text_indentation(text):
    """Prints 2 lines after . or : or ?"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
