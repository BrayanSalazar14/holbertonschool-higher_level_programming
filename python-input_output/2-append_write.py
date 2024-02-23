#!/usr/bin/python3
"""
Module that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str): The path of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a+", encoding="utf-8") as file:
        return file.write(text)
