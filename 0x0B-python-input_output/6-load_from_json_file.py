#!/usr/bin/python3
"""Defines an object creating function"""
import json


def load_from_json_file(filename):
    """Returns an object created from a json file"""
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        return (json.loads(text))
