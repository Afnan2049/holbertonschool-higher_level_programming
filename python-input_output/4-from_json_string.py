#!/usr/bin/python3
"""
This module contains a function that converts a JSON string to an object.
"""
import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        any: The Python data structure represented by my_str.
    """
    return json.loads(my_str)
