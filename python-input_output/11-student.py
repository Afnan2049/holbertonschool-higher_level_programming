#!/usr/bin/python3
"""
This module defines a Student class with filtering and reload methods.
"""


class Student:
    """
    Defines a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student instance.

        Args:
            first_name (str): The first name.
            last_name (str): The last name.
            age (int): The age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings representing attribute names.

        Returns:
            dict: The filtered or full dictionary of the student.
        """
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            res = {}
            for key in attrs:
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary where keys match attribute names.
        """
        for key, value in json.items():
            setattr(self, key, value)
