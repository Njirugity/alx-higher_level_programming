#!/usr/bin/python3
"""Defines a JSON string to object function. """
import json


def from_json_string(my_str):
    """Return a object"""
    return (json.loads(my_str))
