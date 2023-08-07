#!/usr/bin/python3
"""This module ensure persistent object storage"""
from json import dump, loads


class FileStorage:
    """Class to serialize and deserialize instances"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """
        Return all objects
        Returns: a dictionary of all objects
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        Sets a new object

        Args:
            obj (any): any instance of an object
        """
        obj_key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """ Serializes the objects to a file """
        obj_to_file = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        
        with open(self.__file_path, "w") as file:
            dump(obj_to_file, file)
