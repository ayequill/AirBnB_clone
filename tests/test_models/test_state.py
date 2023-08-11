#!/usr/bin/python3
""" Test Cases for State """
from tests.test_models import test_base_model
from models.state import State


class TestState(test_base_model.BaseModelTestCases):
    """ Test Cases for State """

    def setUp(self):
        """ Set up """
        super().setUp()
        self.state = State()

    def test_state_name(self):
        """ Test State name """
        self.state.name = 'Snake land'
        self.assertIsInstance(self.state.name, str)

    def test_state_to_dict(self):
        """ Test State to dict """
        self.assertTrue(self.state.name in self.state.to_dict().values())

    # def test_state_name_with_number(self):
    #     """ Test State name with number """
    #     with self.assertRaises(ValueError):
    #         self.state.name = 100
