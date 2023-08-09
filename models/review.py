#!/usr/bin/python3
""" This module contains the Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class representing a review """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
