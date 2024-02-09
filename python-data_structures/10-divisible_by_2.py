#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    myListCpy = []

    for index in my_list:
        if index % 2 == 0:
            myListCpy.append(True)
        else:
            myListCpy.append(False)
    return myListCpy
