#!/usr/bin/python3
"""Base class """

import json
import turtle


class Base:
    """
    Base class for managing object IDs and file I/O.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with a unique ID.

        Args:
            id (int): The ID to assign to the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert JSON string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaires)

    @staticmethod
    def from_json_string(json_string):
        """JSON to object"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.title("Rectangles and Squares")

        t = turtle.Turtle()

        def draw_rectangle(x, y, width, height):
            t.penup()
            t.goto(x, y)
            t.pendown
            for _ in range(2):
                t.forward(width)
                t.right(90)
                t.forward(height)
                t.right(90)

        def draw_sqaure(x, y, side_length):
            t.penup()
            t.goto(x, y)
            t.pendown()
            for _ in range(4):
                t.forward(side_length)
                t.right(90)

        for rectangle in list_rectangles:
            draw_rectangle(
                    rectangle.x,
                    rectangle.y,
                    rectangle.width,
                    rectangle.height
            )
        
        for square in list_sqaures:
            draw_square(square.x, square.y, square.size)

        turtle.mainloop()

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects to a JSON file.

        Args:
            cls (class): The class of the objects.
            list_objs (list): The list of objects to be saved.
        """
        if list_objs is None:
            list_dictionary = []
        else:
            list_dictionary = [obj.to_dictionary() for obj in list_objs]

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dictionary))

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance of the class based on the given dictionary.

        Args:
            dictionary (dict): A dictionary containing
            the attributes of the instance.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads instances from a JSON file and returns a list of instances.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, "r", encoding="utf-8") as f:
                json_string = f.read()
                list_dicts = cls.from_json_string(json_string)
                instances = []
                for d in list_dicts:
                    instance = cls.create(**d)
                    instances.append(instance)
                return instances
        except IOError:
            return []
