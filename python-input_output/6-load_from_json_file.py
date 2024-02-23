#!/usr/bin/python3
"""
Module that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”

    Args:
        filename (str): The name of the file to write to.
            If the file already exists, its contents will be overwritten.
            If the file does not exist, a new file will be created.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
