#!/usr/bin/python3
"""
Module 7-base_geometry.py
"""


class BaseGeometry:
    """
    Empty class definition
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validation(self, name, value):
        """
        name (str): The name of the value.
        value: The value to be validated.
        """

        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
