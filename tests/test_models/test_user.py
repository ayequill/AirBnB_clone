#!/usr/bin/python3
""" Test Cases for User class """
from unittest import TestCase
from tests.test_models import test_base_model
from models.user import User


class TestUser_with_basemodel(test_base_model.BaseModelTestCases):
    """ Testcases for the user class """

    def setUp(self):
        """ Set Up """
        super().setUp()

    def tearDown(self):
        """ Cleanup """
        super().tearDown()


class TestUser(TestCase):
    def setUp(self):
        """ set Up """
        self.user = User()

    def test_user_email(self):
        """ Test user email """
        # self.user.email = 'test@email.com'
        self.assertIsInstance(self.user.email, str)

    def test_first_name(self):
        """ Test first name """
        # self.user.first_name = 'Test'
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name(self):
        """ Test last name """
        # self.user.last_name = 'Case'
        self.assertIsInstance(self.user.last_name, str)

    def test_password(self):
        """ Test password """
        # self.user.password = 'password'
        self.assertIsInstance(self.user.password, str)
