#!/usr/bin/python3
"""This module ensure persistent object storage"""
from json import dump, load
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from console_misc import classes


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
        obj_to_file = {key: value.to_dict()
                       for key, value in FileStorage.__objects.items()}

        with open(self.__file_path, "w") as file:
            dump(obj_to_file, file)

    def reload(self):
        """ Deserializes a file and converts it into instances"""
        # classes = {
        #     'BaseModel': BaseModel,
        #     'User': User,
        #     'Place': Place,
        #     'City': City,
        #     'Amenity': Amenity,
        #     'Review': Review,
        #     'State': State,
        # }

        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = load(f)
                for key, val in temp.items():
                    cls_name = classes[val['__class__']]
                    FileStorage.__objects[key] = cls_name(**val)
        except IOError:
            pass
