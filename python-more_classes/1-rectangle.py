#!/usr/bin/python3
"""
Define rectangle properties
"""


class Rectangle:
    """
    A class representing a rectangle with width and height attributes.

    Attributes:
        _width (int): Private attribute representing the width of the rectangle.
        _height (int): Private attribute representing the height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Optional, the width of the rectangle (default is 0).
            height (int): Optional, the height of the rectangle (default is 0).
        """
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

