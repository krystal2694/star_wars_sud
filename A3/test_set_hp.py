from unittest import TestCase
from rebel import set_hp
from rebel import rebel


class TestSetHp(TestCase):
    def test_set_hp_with_0(self):
        set_hp(0)
        self.assertEqual(rebel["HP"], 0)

    def test_set_hp_with_positive_int(self):
        set_hp(8)
        self.assertEqual(rebel["HP"], 8)

    def test_set_hp_with_negative_int(self):
        set_hp(-12)
        self.assertEqual(rebel["HP"], -12)
