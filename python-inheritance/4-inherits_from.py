#!/usr/bin/python3
"""
Module 4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
