from unittest import TestCase
from imperial import set_hp
from imperial import imperial_forces
import imperial


class TestSetHp(TestCase):
    def test_set_hp_with_0(self):
        for i in range(len(imperial_forces)):
            set_hp(i, 0)
            self.assertIs(imperial_forces[i]["HP"], 0)

    def test_set_hp_with_positive_int(self):
        for i in range(len(imperial_forces)):
            set_hp(i, 8)
            self.assertIs(imperial_forces[i]["HP"], 8)

    def test_set_hp_with_negative_int(self):
        for i in range(len(imperial_forces)):
            set_hp(i, -12)
            self.assertEqual(imperial_forces[i]["HP"], -12)

    def test_set_hp_changed_from_original(self):
        for i in range(len(imperial_forces)):
            original = imperial.get_hp(i)
            set_hp(i, 3)
            self.assertIsNot(original, imperial_forces[i]["HP"])
