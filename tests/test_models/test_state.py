#!/usr/bin/python3
""" Test Cases for State """
from unittest import TestCase
from tests.test_models import test_base_model
from models.state import State


class TestState_extend_basemodel(test_base_model.BaseModelTestCases):
    """ Test Cases for State """

    def setUp(self):
        """ Set up """
        super().setUp()
        self.state = State()

    def test_state_to_dict(self):
        """ Test State to dict """
        self.state.name = 'Snake land'
        state_obj = self.state.to_dict()
        self.assertTrue(self.state.name in state_obj.values())


class TestState(TestCase):
    """ Test State """

    def test_state_name(self):
        """ Test State name """
        new_state = State()
        new_state.name = 'Snake land'
        self.assertIsInstance(new_state.name, str)
