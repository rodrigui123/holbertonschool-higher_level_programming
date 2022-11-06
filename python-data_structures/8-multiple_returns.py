#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    firstchar = sentence[0]
    sentencelen = len(sentence)
    newTuple = (sentencelen, firstchar)
    return newTuple
