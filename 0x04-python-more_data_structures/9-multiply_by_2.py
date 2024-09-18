#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = a_dictionary.copy()
    newList = list(a_dictionary.keys())
    for i in newList:
        newDict[i] *= 2
    return (newDict)
