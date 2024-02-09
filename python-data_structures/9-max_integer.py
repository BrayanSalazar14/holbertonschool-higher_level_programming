#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None

    """ Con Metodo sort
    length = len(my_list)
    my_list.sort()
    return my_list[length - 1]
    """

    """Sin metodo sort"""
    length = len(my_list)
    numberMax = my_list[0]
    for index in my_list:
        if index > numberMax:
            numberMax = index
    return numberMax
