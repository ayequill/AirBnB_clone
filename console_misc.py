#!/usr/bin/python3
""" This module contains data for the console """
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'City': City,
    'Amenity': Amenity,
    'Review': Review,
    'State': State,
}

commands = [
    'all',
    'show',
    'destroy'
]

attribute_types = {
    'city_id': str,
    'user_id': str,
    'name': str,
    'number_rooms': int,
    'number_bathrooms': int,
    'max_guest': int,
    'price_by_night': int,
    'latitude': float,
    'longitude': float,
    # 'amenity_ids': list,
    'email': str,
    'password': str,
    'first_name': str,
    'last_name': str,
    'place_id': str,
    'text': str,
    'state_id': str
}
