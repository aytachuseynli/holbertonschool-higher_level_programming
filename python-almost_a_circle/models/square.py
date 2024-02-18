#!/usr/bin/python3
"""Square class"""


from models.rectangle import Rectangle


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

    @property
    def size(self):
        """set/get the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.size
        )

    def update(self, *args, **kwargs):
        """
        Updates attributes of the square.

        Args:
            *args: Variable positional arguments for attributes.
            **kwargs: Variable keyword arguments for attributes.
        """
        if args:
            attr_names = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, list_names[i], arg[i])
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
