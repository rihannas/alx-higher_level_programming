#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        char = None
    else:
        char = sentence[0]
    length = len(sentence)
    return char, length
