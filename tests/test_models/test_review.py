#!/usr/bin/python3
""" Test Cases for Review """
from tests.test_models import test_base_model
from models.review import Review


class TestReviews(test_base_model.BaseModelTestCases):
    """ Testcases for Review """

    def setUp(self):
        """ Set up """
        super().setUp()
        self.review = Review()

    def test_place_id(self):
        """ Test Place Id """
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id(self):
        """ Test User Id """
        self.assertIsInstance(self.review.user_id, str)

    def test_text(self):
        """ Test Text """
        self.assertIsInstance(self.review.text, str)
