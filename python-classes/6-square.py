#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Method creation"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value) is not tuple:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        if isinstance(value[0], int) and isinstance(value[1], int):
            if value[0] >= 0 and value[1] >= 0:
                self.__position = (value[0], value[1])
            else:
                print("position must be a tuple of 2 " +
                      "positive integers", end="")
                raise TypeError
        else:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError

    def my_print(self):
        if self.__size > 0:
            if self.__position[1] > 0:
                print("" * self.__position[1])
            for index in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print()
