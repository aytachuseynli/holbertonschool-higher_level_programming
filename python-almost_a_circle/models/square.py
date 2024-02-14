#!/usr/bin/python3
"""Square class"""


from rectangle import Rectangle


class Square(Rectangle):
    """
    Square class representing a square shape.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square.
            y (int): Y-coordinate of the square.
            id (int): ID of the square.
        """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """
        Updates attributes of the square.

        Args:
            *args: Variable positional arguments for attributes.
            **kwargs: Variable keyword arguments for attributes.
        """
        if args:
            attr_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Converts the square to a dictionary.

        Returns:
            dict: Dictionary representation of the square.
        """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def get_size(self):
        """
        Gets the size of the square.

        Returns:
            int: Size of the square.
        """
        return self.width

    def set_size(self, size):
        """
        Sets the size of the square.

        Args:
            size (int): Size to set for the square.
        """
        self.width = size
        self.height = size

    size = property(get_size, set_size)

