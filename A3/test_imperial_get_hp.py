from unittest import TestCase
from imperial import get_hp
from imperial import imperial_forces


class TestGetHp(TestCase):
    def test_get_hp_return_corresponds_to_index(self):
        for i in range(len(imperial_forces)):
            self.assertIs(get_hp(i), imperial_forces[i]["HP"])

    def test_get_hp_return_type(self):
        for i in range(len(imperial_forces)):
            self.assertIsInstance(get_hp(i), int)

    def test_get_hp_with_non_int_objects(self):
        with self.assertRaises(TypeError):
            get_hp("")
            get_hp(5.6)

    def test_get_hp_with_index_greater_than_length_of_imperial_forces_list(self):
        with self.assertRaises(IndexError):
            get_hp(12)
