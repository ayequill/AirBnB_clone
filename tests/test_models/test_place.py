#!/usr/bin/python3
""" Test Cases for Place """
from tests.test_models import test_base_model
from models.place import Place


class TestPlace(test_base_model.BaseModelTestCases):
    """ Testcases for Place """

    def setUp(self):
        """ Set up """
        super().setUp()
        self.place = Place()

    def test_city_id(self):
        """ Test city id """
        self.assertIsInstance(self.place.city_id, str)

    def test_name(self):
        """ Test name """
        self.assertIsInstance(self.place.name, str)

    def test_user_id(self):
        """ Test user id """
        self.assertIsInstance(self.place.user_id, str)

    def test_number_rooms(self):
        """ Test number of rooms """
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms(self):
        """ Test number of bathrooms """
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest(self):
        """ Test max guest """
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night(self):
        """ Test price by night """
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude(self):
        """ Test latitude """
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude(self):
        """ Test longitude """
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids(self):
        self.assertIsInstance(self.place.amenity_ids, list)
