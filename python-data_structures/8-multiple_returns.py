#!/usr/bin/python3
def multiple_returns(sentence):

    if sentence == "":
        return 0, None

    length = len(sentence)
    finalTuple = (sentence[0])
    return length, finalTuple
