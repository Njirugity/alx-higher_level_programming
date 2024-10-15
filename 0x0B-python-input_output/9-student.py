#!/usr/bin/python3
"""Defines a student class."""


class Student:
    """Represents a student class."""
    def __init__(self, first_name, last_name, age):
        """Initializes object
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """Retrieve a dictionary representaion of a student"""
        return self.__dict__
