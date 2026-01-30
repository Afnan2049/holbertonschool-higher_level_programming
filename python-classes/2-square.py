#!/usr/bin/python3
"""Module defining a square class with size validation"""


class Square:
    """Representing a square with optional size.
    
    Args:
    size (int): size of the square

    Raises:
    TypeError: If size is not an int.
    ValueError: if size < 0.
    """
    if not instance (size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    self.__size = size