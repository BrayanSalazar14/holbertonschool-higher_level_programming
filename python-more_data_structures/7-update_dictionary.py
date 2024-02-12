#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for index in range(len(a_dictionary)):
        if index != key:
            a_dictionary[key] = value 
    return a_dictionary
