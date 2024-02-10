#!/usr/bin/python3
"""
Read file module
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.
    """

    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
