#!/usr/bin/python3
"""Defines the base model class"""
import json


class Base:
    """Represents the class Base. The base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance
        Args:
        id: The identity of an instance
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base. __nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file"""
        fn = cls.__name__ + ".json"
        with open(fn, "w") as jsonfile:
            if list_objs:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
            else:
                jsonfile.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string"""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`."""
        fn = str(cls.__name__) + ".json"
        try:
            with open(fn, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
