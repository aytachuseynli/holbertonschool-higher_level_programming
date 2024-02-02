#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The size of the square (private).
        """
        self.__size = size
