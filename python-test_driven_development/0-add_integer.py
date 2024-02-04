#!/usr/bin/python3
"""
Write a function that adds 2 integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Default is 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    # Check if a is an integer or float; raise TypeError if not
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")

    # Check if b is an integer or float; raise TypeError if not
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    # Cast a and b to integers and return their sum
    return int(a) + int(b)
