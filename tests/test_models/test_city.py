#!/usr/bin/python3
""" Test Cases for City Class """
from tests.test_models import test_base_model
from models.city import City


class TestCityClass(test_base_model.BaseModelTestCases):
    """ Test cases for City Class """

    def setUp(self):
        """ Set up """
        super().setUp()
        self.test_city = City()

    def tearDown(self):
        """ Clean up """
        super().tearDown()

    def test_state_id(self):
        """ Test state id type """
        self.assertIsInstance(self.test_city.state_id, str)

    def test_name(self):
        """ Test name type """
        self.assertIsInstance(self.test_city.name, str)
