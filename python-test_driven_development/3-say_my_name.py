#!/usr/bin/python3
"""
This is the "say_my_name" module.
The add module supplies one function, say_my_name().  For example,
>>> say_my_name("Brayan", Salazar)
My name is Brayan Salazar
"""


def say_my_name(first_name, last_name=""):
    """Function with two parameters
    print the string complete
    """
    if isinstance(first_name, str):
        if isinstance(last_name, str):
            print("My name is {} {}".format(first_name, last_name))
        else:
            raise TypeError("last_name must be a string")
    else:
        raise TypeError("first_name must be a string")
