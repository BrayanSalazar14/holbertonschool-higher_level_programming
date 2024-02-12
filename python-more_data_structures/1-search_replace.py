#!/usr/bin/python3
def search_replace(my_list, search, replace):
    listChanges = []
    for index in my_list:
        if index == search:
            listChanges.append(replace)
        else:
            listChanges.append(index)
    return listChanges
