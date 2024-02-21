#!/usr/bin/python3
"""
Class  that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class, otherwise False
"""


def inherits_from(obj, a_class):
    """_summary_

    Args:
        obj: instance
        a_class: Type
    Returns:
        _type_:  returns True if the object is an instance
        of a class that inherited
        (directly or indirectly) from the specified class, otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
