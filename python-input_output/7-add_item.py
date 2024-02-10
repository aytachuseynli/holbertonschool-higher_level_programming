#!/usr/bin/python3
"""
Load, save, add
"""


import json
import sys
import os

# Importing the functions directly
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_items_to_list_and_save(filename, *items):
    """
    Adds items to a list and saves it to a file.
    """
    try:
        existing_data = load_from_json_file(filename)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    existing_data.extend(items)
    save_to_json_file(existing_data, filename)


if __name__ == '__main__':
    # Default filename if not provided as an argument
    default_filename = 'add_item.json'

    # Use the provided filename or the default one
    filename = sys.argv[1] if len(sys.argv) > 1 else default_filename

    # Extract items from command-line arguments
    items = sys.argv[2:]

    # Add items to the list and save to the file
    add_items_to_list_and_save(filename, *item)
