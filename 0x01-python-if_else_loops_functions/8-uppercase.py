#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord(char) not in range(65, 91):
            char = ord(char) + 32
            char = chr(char)
            print('{}'.format(char))
    print()
