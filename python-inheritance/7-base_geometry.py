#!/usr/bin/python3
"""
Class BaseGeometry whit two methods
"""


class BaseGeometry:
    """Class with two methods, area and integer_validation
    """

    def are(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
