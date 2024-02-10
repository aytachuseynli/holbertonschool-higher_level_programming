#!/usr/bin/python3
"""
Write to a file module
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and 
    returns the number of characters written.
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        num_chars_written = file.write(text)

    return num_chars_written
