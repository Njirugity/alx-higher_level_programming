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

    def to_json(self, attrs=None):
        """Retrieve a dictionary representaion of a student"""
        obj = self.__dict__
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return obj

            my_list = {}
            for i in range(len(attrs)):
                for j in obj:
                    if attrs[i] == j:
                        my_list[j] = obj[j]
            return my_list

        return obj

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for atr in json:
            self.__dict__[atr] = json[atr]
