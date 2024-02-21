#!/usr/bin/python3
"""Funcion that returns the list of available attributes and methods
"""


def lookup(obj):
    """Lookup all attributes in my class

    Args:
        obj: object class

    Returns:
        returns the list of available attributes and methods of an object
    """
    return [index for index in dir(obj)]
