#!/usr/bin/python3
"""Module containing BaseModel Class"""
from uuid import uuid4
from datetime import datetime as date


class BaseModel:
    """Class for the BaseModel"""
    __current_date = date.now()

    def __init__(self, *args, **kwargs):
        """Constructor for Base Model"""
        self.id = str(uuid4())
        self.created_at = date.now()
        self.updated_at = date.now()
        if kwargs:
            kwargs.pop("__class__")
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    setattr(self, k, date.fromisoformat(v))
                    continue
                setattr(self, k, v)

    def save(self):
        """
        Saves the model at the current date
        """
        self.updated_at = date.now()

    def to_dict(self):
        """
        Returns a dictionary of model attributes

        Returns:
            dict: a dictionary of model attributes
        """
        dictionary = self.__dict__
        dictionary.update({
            '__class__': self.__class__.__name__,
            'created_at': self.updated_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        })
        return dictionary

    def __str__(self):
        """
        Returns a string representation of
        object

        Returns:
            str: string representation of object
        """
        return "[{}] ({}) {}>".format(
            self.__class__.__name__,
            self.id, self.__dict__)
