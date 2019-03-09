from unittest import TestCase
from imperial import get_name
from imperial import imperial_forces


class TestGetName(TestCase):
    def test_get_name_return_name_corresponds_to_index(self):
        for i in range(len(imperial_forces)):
            self.assertIs(get_name(i), imperial_forces[i]["Name"])

    def test_get_name_return_type(self):
        for i in range(len(imperial_forces)):
            self.assertIsInstance(get_name(i), str)
