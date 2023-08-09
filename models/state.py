#!/usr/bin/python3
""" This module contains the State class """
from models.base_model import BaseModel


class State(BaseModel):
    """ Class representing States """
    name: str = ""
