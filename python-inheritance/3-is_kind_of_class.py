#!/usr/bin/python3
"""
Class  that returns True if the object is an instance of, or
if the object is an instance of a class that inherited from,
the specified class, otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: instance
        a_class: Type

    Returns:
        _type_: Trueif the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class
    """
    return isinstance(obj, a_class)
