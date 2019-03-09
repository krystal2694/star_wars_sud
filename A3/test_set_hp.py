from unittest import TestCase
from rebel import set_hp
import rebel


class TestSetHp(TestCase):
    def test_set_hp_with_0(self):
        set_hp(0)
        self.assertEqual(rebel.rebel["HP"], 0)

    def test_set_hp_with_positive_int(self):
        set_hp(8)
        self.assertEqual(rebel.rebel["HP"], 8)

    def test_set_hp_with_negative_int(self):
        set_hp(-12)
        self.assertEqual(rebel.rebel["HP"], -12)

    def test_set_hp_changed_from_original(self):
        original = rebel.get_hp()
        set_hp(4)
        self.assertIsNot(original, rebel.rebel["HP"])
