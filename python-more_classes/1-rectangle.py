#!/usr/bin/python3
""" Rectangle class"""


class Rectangle:
    """Defines a rectangle with width and height attributes. """
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        """Getter method for the width attribute"""
        return self._width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter method for the height attribute. """
        return self._height

    @height.setter
    def height(self, value):
        """Setter method for the width attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
