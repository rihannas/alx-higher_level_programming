#!/usr/bin/python3
def multiple_returns(sentence):
    tup = ()
    if sentence == "":
        tup = None
    else:
        tup = len(sentence), sentence[0]
    return tup
