#!/usr/bin/python3
"""
Module that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
     Read the content of a file and print it to the console.
    Args:
        filename (str, optional): The path of the file to be read.
        If not provided, it will read from the standard input (stdin).
    """
    with open(filename, "r", encoding="utf-8") as archivo:
        print(archivo.read(), end="")
