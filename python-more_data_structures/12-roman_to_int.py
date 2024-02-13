#!/usr/bin/python3
def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    acronym = dict([
        ("I", 1), ("V", 5), ("X", 10),
        ("L", 50), ("C", 100), ("D", 500), ("M", 1000)
        ])

    container = []
    for symbol in roman_string:
        container.append(acronym[symbol])

    for index in range(len(container) - 1):
        if container[index] < container[index + 1]:
            container[index] = container[index] * - 1

    total = 0
    for index in container:
        total += index

    return total


"""Other form
def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    acronym = dict([
        ("I", 1), ("V", 5), ("X", 10),
        ("L", 50), ("C", 100), ("D", 500), ("M", 1000)
        ])
    total = 0
    prev_value = 0
    for symbol in reversed(roman_string):
        value = acronym[symbol]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total"""
