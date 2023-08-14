#!/usr/bin/python3
""" Test Cases for Amenity """
from tests.test_models import test_base_model
from models.amenity import Amenity


class TestAmenity(test_base_model.BaseModelTestCases):
    """ Testcases for Amenity """

    def setUp(self):
        """ Set up """
        super().setUp()
        self.amenity = Amenity()

    def test_amenity_name(self):
        """ Test name """
        self.assertIsInstance(self.amenity.name, str)
