#!/usr/bin/python3
"""
Module 11-square.py
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inheriting from Rectangle
    """
    def __init__(self, size):
        """
        Initializes a Square instance
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns the square description
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size ** 2


if __name__ == "__main__":
    s = Square(4)
    print(s)
    print("Area:", s.area())
