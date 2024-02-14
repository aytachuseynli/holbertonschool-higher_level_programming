#!/usr/bin/python3
"""Base class """

import json


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

    @classmethod
    def create(cls, dictionary):
        """
        Creates a new instance from a dictionary.

        Args:
            dictionary (dict): Dictionary containing attribute values.

        Returns:
            Base: An instance of the class.
        """
        obj = cls.__new__(cls)
        obj.update(**dictionary)
        return obj

    @classmethod
    def loadfromfile(cls):
        """
        Loads instances from a JSON file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return [cls.create(d) for d in data]
        except FileNotFoundError:
            return []

    @classmethod
    def savetofile(cls, listobjs):
        """
        Saves instances to a JSON file.

        Args:
            listobjs (list): List of instances to be saved.
        """
        filename = cls.__name__ + ".json"
        data = [obj.to_dictionary() for obj in listobjs]
        with open(filename, 'w') as file:
            json.dump(data, file)
