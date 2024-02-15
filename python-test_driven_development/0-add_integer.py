#!/usr/bin/python3
"""
This is the "add_integer" module.
The add module supplies one function, add_integer().  For example,
>>> add_integer(3, 3)
6
"""


def add_integer(a, b=98):
    """Returns an integer:
    The result for a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(int(a) + int(b))
