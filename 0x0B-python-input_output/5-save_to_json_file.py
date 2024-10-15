#!/usr/bin/python3
""" Define text writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a file
    Args:
        my_obj: oject to write to file after json representation of the object
        filename: file to be written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
