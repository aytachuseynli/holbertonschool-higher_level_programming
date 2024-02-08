#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Define a rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialized method"""
        self.width = width
        self.height = height

     def __str__(self):
        """ str """
        if self.width == 0 or self.height == 0:
            return " "
        return '\n'.join(['#' * self.width for _ in range(self.height)])

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Rectangle perimeter"""
        return (2 * (self.width + self.height)
                if self.width != 0 and self.height != 0 else 0)
        
