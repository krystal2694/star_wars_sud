from unittest import TestCase
from imperial import set_hp
from imperial import imperial_forces
import imperial


class TestSetHp(TestCase):
    def setUp(self):
        """Reset each enemy HP to 5 before each unit test."""
        # This makes it clear what the value of their HP is before the function is called
        for i in range(len(imperial_forces)):
            imperial_forces[i]["HP"] = 5

    def test_set_hp_with_0(self):
        for i in range(len(imperial_forces)):
            set_hp(i, 0)
            self.assertIs(imperial_forces[i]["HP"], 0)

    def test_set_hp_with_positive_int(self):
        for i in range(len(imperial_forces)):
            set_hp(i, 8)
            self.assertIs(imperial_forces[i]["HP"], 8)

    def test_set_hp_changed_from_original(self):
        for i in range(len(imperial_forces)):
            original = imperial.get_hp(i)
            set_hp(i, 3)
            self.assertIsNot(original, imperial_forces[i]["HP"])
