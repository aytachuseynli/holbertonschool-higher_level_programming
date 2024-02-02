#!/usr/bin/python3
"""
Define a class Square with size validation.
"""


class Square:
    """
    Represents a square with size validation.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square. Default is 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__validate_size(value)
        self.__size = value

    def __validate_size(self, value):
        """
        Validates the size attribute.

        Args:
            value (int): The size to be validated.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
