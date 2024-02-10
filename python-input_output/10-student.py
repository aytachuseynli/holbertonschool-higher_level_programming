#!/usr/bin/python3
"""
Student to JSON with filter
"""


class Student:
    """
    Student class with enhanced to_json method.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: getattr(self, key)
                    for key in attrs
                    if hasattr(self, key)}
