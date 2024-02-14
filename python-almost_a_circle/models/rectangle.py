#!/usr/bin/python3
"""Rectangle class"""


from base import Base


class Rectangle(Base):
    """
    Rectangle class representing a rectangle shape.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle.
            y (int): Y-coordinate of the rectangle.
            id (int): ID of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args, **kwargs):
        """
        Updates attributes of the rectangle.

        Args:
            *args: Variable positional arguments for attributes.
            **kwargs: Variable keyword arguments for attributes.
        """
        if args:
            attr_names = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Displays the rectangle using '#' characters.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def to_dictionary(self):
        """
        Converts the rectangle to a dictionary.

        Returns:
            dict: Dictionary representation of the rectangle.
        """
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

