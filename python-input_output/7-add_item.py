#!/usr/bin/python3
"""
Load, save, add: This script loads a list from a JSON file (if it exists),
or creates a new list, adds command-line arguments to it, and then saves the
updated list back to the file in JSON format.
"""


import json
import sys
import os


def save_to_json_file(my_obj, filename):
    """
    Writes the JSON representation of an object to a text file (UTF8).
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))

def load_from_json_file(filename):
    """
    Creates an object from a "JSON file".
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)

def add_items_to_list_and_save(filename, *items):
    """
    Load an existing list from a file or create a new list,
    add items to it, and save the updated list to the file.
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
    add_items_to_list_and_save(filename, *items)

