from unittest import TestCase
from imperial import get_dexterity
from imperial import imperial_forces


class TestGetDexterity(TestCase):
    def test_get_dexterity_return_corresponds_to_index(self):
        for i in range(len(imperial_forces)):
            self.assertIs(get_dexterity(i), imperial_forces[i]["Dexterity"])

    def test_get_dexterity_return_type(self):
        for i in range(len(imperial_forces)):
            self.assertIsInstance(get_dexterity(i), int)

    def test_get_dexterity_with_non_int_objects(self):
        with self.assertRaises(TypeError):
            get_dexterity("")
            get_dexterity(1.4)

    def test_get_dexterity_with_index_greater_than_length_of_imperial_forces_list(self):
        with self.assertRaises(IndexError):
            get_dexterity(20)

