#!/usr/bin/python3

"""
Create a function def roman_to_int(roman_string):
that converts a Roman numeral to an integer.
"""


def roman_to_int(roman_string):
    if type(roman_string) is not str or None:
        return 0

    else:
        romInt = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        length = len(roman_string)

        for idx in range(0, length):
            current = roman_string[idx]
            if idx < (length - 1):
                next = roman_string[idx + 1]
                if romInt[current] >= romInt[next]:
                    total = total + romInt[current]
                else:
                    total = total - romInt[current]
            elif idx == (length - 1):
                total = total + romInt[current]
        return total
