#!/usr/bin/python3
"""
This module contains a function that reads a text file and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a UTF8 text file and prints its content to the standard output.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
