#!/usr/bin/python3
def multiple_returns(sentence):
    tup = ()
    if len(sentence) == 0:
        tup = None
    else:
        tup = sentence[0], len(sentence)
    return tup
