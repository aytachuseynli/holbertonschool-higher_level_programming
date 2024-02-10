#!/usr/bin/python3
"""
Module 7-base_geometry.py
"""


class BaseGeometry:
    """
    class definition
    """


    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer".format(name))

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0".format(name))
