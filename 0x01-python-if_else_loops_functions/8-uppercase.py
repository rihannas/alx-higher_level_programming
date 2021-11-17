#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if (ord(letter) >= 97) and (ord(letter) <= 122):
            letter = chr(ord(char) - 32)
        print("{}".format(letter), end="")
