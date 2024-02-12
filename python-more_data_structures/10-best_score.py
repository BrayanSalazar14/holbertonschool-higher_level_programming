#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)


"""Other form
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None

    bestScore = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == bestScore:
            return key
"""
