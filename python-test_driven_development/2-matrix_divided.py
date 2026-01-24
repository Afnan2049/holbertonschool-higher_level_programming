#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor (div).
    
    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The number to divide by.
        
    Returns:
        list: A new matrix with results rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Check if matrix is a list and not empty
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    # 2. Check each row and its elements
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    # 3. Check row sizes (compare to the length of the first row)
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # 4. Check div type
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 5. Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 6. Perform the operation
    return [[round(item / div, 2) for item in row] for row in matrix]
