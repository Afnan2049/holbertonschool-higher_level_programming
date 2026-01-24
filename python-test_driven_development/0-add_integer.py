#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The function handles floats by casting them to integers first.
It includes validation for input types to ensure only numbers are processed.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), defaults to 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b are not integers, floats, or are NaN.
    """
    # Check if a is not a number or is NaN
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if a != a:  # This is the most efficient way to check for NaN in Python
        raise TypeError("a must be an integer")

    # Check if b is not a number or is NaN
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if b != b:  # Logic: NaN is the only value that does not equal itself
        raise TypeError("b must be an integer")

    return int(a) + int(b)
