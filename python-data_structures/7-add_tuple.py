#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = (0, 0)
    b = (0, 0)
    lengthA = len(tuple_a)
    lengthB = len(tuple_b)

    if lengthA == 0:
        a
    elif lengthA == 1:
        a = (tuple_a[0], 0)
    elif lengthA >= 2:
        a = (tuple_a[0], tuple_a[1])

    if lengthB == 0:
        b
    elif lengthB == 1:
        b = (tuple_b[0], 0)
    elif lengthB >= 2:
        b = (tuple_b[0], tuple_b[1])

    return(a[0] + b[0], a[1] + b[1])
