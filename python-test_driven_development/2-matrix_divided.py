#!/usr/bin/python3
"""
2-matrix_divided.py, tests/2-matrix_divided.txt
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): Matrix of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: New matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if div is not a number (integer or float).
        TypeError: If each row of the matrix doesn't have the same size.
        ZeroDivisionError: If div is equal to 0.
    """
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
