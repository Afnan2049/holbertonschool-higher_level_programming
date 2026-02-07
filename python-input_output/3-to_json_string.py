#!/usr/bin/python3
"""
This module contains a function that converts an object to a JSON string.
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized.

    Returns:
        str: The JSON string representation of my_obj.
    """
    return json.dumps(my_object)
