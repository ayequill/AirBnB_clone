#!/usr/bin/python3
"""Module containing BaseModel Class"""
from uuid import uuid4
from datetime import datetime as date


class BaseModel:
    """Class for the BaseModel"""
    __current_date = date.now()

    def __init__(self):
        """Constructor for Base Model"""
        self.id = str(uuid4())
        self.created_at = date.now()
        self.updated_at = date.now()
