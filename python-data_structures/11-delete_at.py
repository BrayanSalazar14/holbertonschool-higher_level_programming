#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list

    length = len(my_list)
    for index in range(length):
        if index == idx:
            my_list.remove(my_list[index])
    return my_list
