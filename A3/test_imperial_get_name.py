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

    def test_get_name_with_non_int_objects(self):
        with self.assertRaises(TypeError):
            get_name("")
            get_name(2.3)

    def test_get_name_with_index_greater_than_length_of_imperial_forces_list(self):
        with self.assertRaises(IndexError):
            get_name(9)
