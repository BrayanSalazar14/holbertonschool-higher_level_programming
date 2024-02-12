#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    newSet = set()
    commondElem = set_1.intersection(set_2)
    for elem in set_1:
        for elem2 in set_2:
            if elem not in commondElem and elem2 not in commondElem:
                newSet.add(elem)
                newSet.add(elem2)
    return newSet
