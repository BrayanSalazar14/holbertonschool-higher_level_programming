#!/usr/bin/python3
"""
Module that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: The object to be written to the file.
        filename (str): The name of the file to write to.
            If the file already exists, its contents will be overwritten.
            If the file does not exist, a new file will be created.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
