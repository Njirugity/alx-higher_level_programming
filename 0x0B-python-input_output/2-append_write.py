#!/usr/bin/python3
""" Define a string appending function"""


def append_write(filename="", text=""):
    """Append a strng into a text file
    Args:
        filename: Name of file to write to
        text: String to write to file
    Returns:
        Number of characters writen
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
