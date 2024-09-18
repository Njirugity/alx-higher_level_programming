#!/usr/bin/python3
def uniq_add(my_list=[]):
    newList = []
    sum = 0
    for n in my_list:
        if n not in newList:
            sum += n
            newList.append(n)
    return sum
