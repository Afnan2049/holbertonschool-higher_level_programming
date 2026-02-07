#!/usr/bin/python3
"""
This module contains a function that creates an Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        any: The Python object representation of the JSON file content.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
