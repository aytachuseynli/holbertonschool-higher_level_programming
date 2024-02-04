#!/usr/bin/python3
"""
Write a function that adds 2 integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float).
        b (int or float, optional).

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
 
    a = int(a)
    b = int(b)

    return a + b
