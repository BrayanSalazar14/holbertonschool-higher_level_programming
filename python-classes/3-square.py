#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Creation of the methods"""

    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                print("size must be >= 0", end="")
                raise ValueError
            else:
                self.__size = size
        else:
            print("size must be an integer", end="")
            raise TypeError

    def area(self):
        return self.__size ** 2
