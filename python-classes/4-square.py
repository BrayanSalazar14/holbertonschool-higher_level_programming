#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Method creation"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                print("size must be >= 0", end="")
                raise ValueError
            else:
                self.__size = value
        else:
            print("size must be an integer", end="")
            raise TypeError
