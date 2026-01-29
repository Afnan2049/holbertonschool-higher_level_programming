#!/usr/bin/python
"""
A module defining a class Square with a private size attribute.
Demonstrating basic creation and encapsulation in Python
"""
class Square:
    """
A class defining a square by its size.
Attributes:
__size (any): The size of the square.
    """

    def __int__(self, size):
        """
       Initializing the square with a given size.
       Args:
       size: The size of the square.
        """
        self.__size = size