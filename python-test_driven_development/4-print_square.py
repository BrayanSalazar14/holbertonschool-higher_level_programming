#!/usr/bin/python3
"""
This is the "print_square" module.
The add module supplies one function, print_square().  For example,
>>> print_square(2)
##
##
"""


def print_square(size):
    """Function that prints a square
    Print a square using size
    """
    if isinstance(size, int):
        if size >= 0:
            for index in range(size):
                print("#" * size)
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")


"""Other form"""
"""def print_square(size):"""
#    if isinstance(size, int):
#        if size >= 0:
#            for rows in range(size):
#                for columns in range(size):
#                    print("#", end="")
#               print()
#       else:
#           raise ValueError("size must be >= 0")
#   else:
#       raise TypeError("size must be an integer")
