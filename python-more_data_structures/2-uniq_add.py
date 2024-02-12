#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqueList = []
    for index in my_list:
        if index not in uniqueList:
            uniqueList.append(index)
    return sum(uniqueList)


"""Other form
def uniq_add(my_list=[]):
    uniqueList = set(my_list)
    return sum(uniqueList)
"""
