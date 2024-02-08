#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    myListCopy = list.copy(my_list)
    length = len(myListCopy)

    if idx < 0:
        return myListCopy

    if idx >= length:
        return myListCopy

    for i in range(length):
        if i == idx:
            myListCopy[i] = element
            return myListCopy
