#!/usr/bin/python3
"""This module ensure persistent object storage"""
from json import dump, loads


class FileStorage:
    """Class to serialize and deserialize instances"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        obj_key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[obj_key] = obj
