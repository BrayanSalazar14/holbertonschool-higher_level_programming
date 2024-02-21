#!/usr/bin/python3
"""
Class function that returns True if the object is exactly an instance
of the specified class, otherwise False
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: instance
        a_class: Type

    Returns:
        _type_: True, if the object is exactly an
        instance of the specified class
        Otherwise False
    """
    return type(obj) is a_class
