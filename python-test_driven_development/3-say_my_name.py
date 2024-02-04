#!/usr/bin/python3

"""
3-say_my_name.py, tests/3-say_my_name.txt
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Default is an empty string.

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not all(isinstance(name, str) for name in (first_name, last_name)):
        raise TypeError("first_name must be a string or last_name must be a string")

    full_name = "My name is {} {}".format(first_name, last_name)
    print(full_name)
