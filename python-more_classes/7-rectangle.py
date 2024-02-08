#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Define a rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialized method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """String representation"""
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join(
                [str(self.print_symbol) * self.width for _ in range(self.height)]
        )

    def __repr__(self):
        """repr"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """del"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
