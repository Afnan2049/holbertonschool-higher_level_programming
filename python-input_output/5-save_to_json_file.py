#!/usr/bin/python3
"""
This module contains a function that writes an Obj to a file using JSON.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The name of the file to create/write to.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
