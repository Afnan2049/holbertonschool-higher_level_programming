#!/usr/bin/env python3
import csv
import json

"""
Module for converting CSV data to JSON format.
"""

def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it to a JSON file.
    
    Args:
        csv_filename (str): The name of the source CSV file.
        
    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        data_list = []
        
        # Open and read the CSV file
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # DictReader uses the first row as dictionary keys
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data_list.append(row)
        
        # Serialize the list of dictionaries to data.json
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)
            
        return True

    except FileNotFoundError:
        return False
    except Exception:
        # Catch-all for other potential issues like permission errors
        return False
