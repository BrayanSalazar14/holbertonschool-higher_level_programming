#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for index in range(len(a_dictionary)):
        if a_dictionary != key:
            a_dictionary[key] = value
        else:
            a_dictionary[index] = value
    return a_dictionary
