#!/usr/bin/env python3
import pickle

"""
Module for serializing and deserializing custom Python objects using pickle.
"""

class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        """Initializes the CustomObject with name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes in a specific format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance to a file using pickle.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, IOError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads a serialized instance of CustomObject from a file.
        
        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                # Verify the loaded object is actually an instance of this class
                if isinstance(obj, cls):
                    return obj
            return None
        except (FileNotFoundError, EOFError, pickle.UnpicklingError, OSError):
            return None
