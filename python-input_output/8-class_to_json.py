#!/usr/bin/python3
"""
module that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary with simple data structure
        suitable for JSON serialization.
    """
    my_dic = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, str, dict, int, bool)):
            my_dic[key] = value
    return my_dic
