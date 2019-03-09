from unittest import TestCase
import rebel


class TestSetHp(TestCase):
    def test_set_hp_with_0(self):
        rebel.set_hp(0)
        self.assertEqual(rebel.rebel["HP"], 0)

    def test_set_hp_with_positive_int(self):
        rebel.set_hp(8)
        self.assertEqual(rebel.rebel["HP"], 8)

    def test_set_hp_with_negative_int(self):
        rebel.set_hp(-12)
        self.assertEqual(rebel.rebel["HP"], -12)
