#!/usr/bin/python3
""" Test Cases for BaseModel """
from os import remove
from json import dump, load
from datetime import datetime as date
from unittest import TestCase
from models.base_model import BaseModel


class BaseModelTestCases(TestCase):
    def setUp(self):
        """ Set up """
        self.model = BaseModel()

    def tearDown(self):
        """ Cleanup """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_create_model(self):
        """ Testing creating a model """
        self.assertIsInstance(self.model, BaseModel)
        # self.assertEqual(type(self.model.id), type(str))

    def test_model_id(self):
        """ Test Model id """
        self.assertIsInstance(self.model.id, str)
        self.assertEqual(len(self.model.id), 36)

    def test_model_date_type(self):
        """ Test Model date type """
        self.assertIsInstance(self.model.created_at, date)
        self.assertIsInstance(self.model.updated_at, date)

    # def test_date_time(self):
    #     f_date = self.model.created_at.isoformat()

    def test_str_repr(self):
        """ Test the __str__ method"""
        cls_name = str(self.model).split(" ")[0]
        self.assertEqual(cls_name, "[BaseModel]")

    # def test_create_model_with_arg(self):
    #     with self.assertRaises(ValueError):
    #         new_model = BaseModel(1)

    def test_create_with_kwargs(self):
        """ Test creating with valid arguments """
        obj_dict = self.model.to_dict()
        new_model = BaseModel(**obj_dict)
        self.assertIsInstance(new_model, BaseModel)
        self.assertFalse("__class__" in new_model.__dict__)

    def test_create_with_bad_key_kwargs(self):
        """ Test creating with bad key arguments """
        bad_kwargs = {'Bad': 'Dict'}
        # with self.assertRaises(KeyError):
        bad_model = BaseModel(**bad_kwargs)
        self.assertFalse(bad_kwargs['Bad'] in bad_model.__dict__)

    def test_create_with_none_args(self):
        """ Test creating with None arguments """
        none_dict = {None: None}
        with self.assertRaises(TypeError):
            new_model = BaseModel(**none_dict)

    def test_to_dict(self):
        """ Test instance to dict conversion """
        obj_to_dict = self.model.to_dict()
        self.assertIsInstance(obj_to_dict, dict)
        self.assertEqual(obj_to_dict["id"], self.model.id)
        self.assertEqual(obj_to_dict["__class__"],
                         self.model.__class__.__name__)
        new_model = BaseModel(**obj_to_dict)
        self.assertIsInstance(new_model, BaseModel)

    def test_save_instance(self):
        """ Test serialization of instance"""
        new_model = BaseModel()
        new_model.save()
        key = new_model.__class__.__name__ + "." + new_model.id
        with open('file.json', 'r') as file:
            j = load(file)
            self.assertEqual(j[key], new_model.to_dict())

    def test_add_attribs_and_serialize(self):
        """ Test add_attribs and serialize """
        self.model.name = 'my_model'
        self.model.number = 89
        self.assertIsInstance(self.model.__dict__['name'], str)
        self.assertIsInstance(self.model.__dict__['number'], int)
        self.model.save()

        key = self.model.__class__.__name__ + "." + self.model.id
        with open('file.json', 'r') as file:
            j = load(file)
            self.assertEqual(j[key], self.model.to_dict())
