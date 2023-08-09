#!/usr/bin/python3
""" Test Cases for BaseModel """
from os import remove
from datetime import datetime as date
from unittest import TestCase
from models.base_model import BaseModel


class BaseModelTestCases(TestCase):
    def setUp(self):
        self.model = BaseModel()

    def tearDown(self):
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_create_model(self):
        """ """
        self.assertIsInstance(self.model, BaseModel)
        # self.assertEqual(type(self.model.id), type(str))

    def test_model_id(self):
        """ """
        self.assertIsInstance(self.model.id, str)
        self.assertEqual(len(self.model.id), 36)

    def test_model_date_type(self):
        """ """
        self.assertIsInstance(self.model.created_at, date)
        self.assertIsInstance(self.model.updated_at, date)

    # def test_date_time(self):
    #     f_date = self.model.created_at.isoformat()

    def test_str_repr(self):
        """ """
        cls_name = str(self.model).split(" ")[0]
        self.assertEqual(cls_name, "[BaseModel]")

    # def test_create_model_with_arg(self):
    #     with self.assertRaises(ValueError):
    #         new_model = BaseModel(1)

    def test_create_with_kwargs(self):
        """ """
        obj_dict = self.model.to_dict()
        new_model = BaseModel(**obj_dict)
        self.assertIsInstance(new_model, BaseModel)
        self.assertFalse("__class__" in new_model.__dict__)

    def test_create_with_none_args(self):
        """ """
        none_dict = {None: None}
        with self.assertRaises(TypeError):
            new_model = BaseModel(**none_dict)

    def test_to_dict(self):
        """ """
        obj_to_dict = self.model.to_dict()
        self.assertIsInstance(obj_to_dict, dict)
        self.assertEqual(obj_to_dict["id"], self.model.id)
        self.assertEqual(obj_to_dict["__class__"],
                         self.model.__class__.__name__)
