#!/usr/bin/python3
"""Define a text file reading function"""


def read_file(filename=""):
    """Print the content of a file."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
