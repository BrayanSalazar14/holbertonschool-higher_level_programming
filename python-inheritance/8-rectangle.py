#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Class Rectangle that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    Instantiation with width and height:
    Args:
        BaseGeometry (Class): Parent class
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
