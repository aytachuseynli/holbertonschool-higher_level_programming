#!/usr/bin/python3
"""
Load, add, save
"""


import json
import sys
import os


from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_items_to_list_and_save(filename, *items):
    """save add load"""
    try:
        existing_data = load_from_json_file(filename)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    existing_data.extend(items)
    save_to_json_file(existing_data, filename)

if __name__ == "__main__":
    default_filename = "add_item.json"
    filename = sys.argv[1] if len(sys.argv) > 1 else default_filename
    items = sys.argv[2:]

    add_items_to_list_and_save(filename, *items)
