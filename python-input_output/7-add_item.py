#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a JSON file.
"""
import sys
import os


# Import functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# 1. Load existing data or start fresh
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# 2. Add arguments (excluding the script name itself at index 0)
items.extend(sys.argv[1:])

# 3. Save back to the file
save_to_json_file(items, filename)
