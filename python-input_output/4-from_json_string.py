#!/usr/bin/python3
"""
Module that returns an object (Python data structure) represented by a
JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string

    Args:
        my_str: String format JSON

    Returns:
        obj: The JSON representation of the string
    """
    return json.loads(my_str)
