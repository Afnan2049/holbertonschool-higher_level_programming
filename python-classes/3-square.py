#!/usr/bin/python3
"""This module defines a Square class and computes its area."""

class Square:
    """Docstring for Square"""

    def __init__(self, size+0):
        """Initialize a Square with optional size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            """
        if not instance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raisw ValueError("size must be >= 0")

            self.__size = size

            def area(self):
                """Return the current area of the square."""
                return self.__size ** 2