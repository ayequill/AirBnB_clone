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
# from console_misc import classes


class FileStorage:
    """Class to serialize and deserialize instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls: BaseModel=None):
        """
        Return all objects
        Returns: a dictionary of all objects
        """
        if cls is None:
            return FileStorage.__objects

        instance_objs = {}
        for key, value in FileStorage.__objects.items():
            if value.__class__ == cls:
                instance_objs[key] = FileStorage.__objects[key]
        return instance_objs

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

        with open(FileStorage.__file_path, "w") as file:
            dump(obj_to_file, file)

    def reload(self):
        """ Deserializes a file and converts it into instances"""
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'City': City,
            'Amenity': Amenity,
            'Review': Review,
            'State': State,
        }

        try:
            # temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = load(f)
                for key, val in temp.items():
                    cls_name = classes[val['__class__']]
                    # FileStorage.__objects[key] = cls_name(**val)
                    self.new(cls_name(**val))
        except IOError:
            pass

    def delete(self, obj=None):
            """Delete objects from the File Storage"""
            if obj is not None:
                key = obj.__class__.__name__ + "." + obj.id
                if key in FileStorage.__objects:
                    del FileStorage.__objects[key]
                    
    def get(self, cls: BaseModel, id: str) -> BaseModel:
        """ Returns an object from file storage """
        key = f"{cls.__name__}.{id}"
        return self.all(cls).get(key)
    
    def count(self, cls: BaseModel=None) -> int:
        return len(self.all(cls)) if cls else len(self.all())
