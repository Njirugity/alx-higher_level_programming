#!/usr/bin/python3
""" Define a string writting function"""


def write_file(filename="", text=""):
    """Write a strng into a text file
    Args:
        filename: Name of file to write to
        text: String to write to file
    Returns:
        Number of characters writen
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
