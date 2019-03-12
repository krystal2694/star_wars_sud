from unittest import TestCase
from rebel import set_hp
from rebel import rebel


class TestSetHp(TestCase):
    def setUp(self):
        """Reset character HP to 10 before each unit test."""
        # This makes it clear what the value of their HP is before the function is called
        rebel["HP"] = 10

    def test_set_hp_with_0(self):
        set_hp(0)
        self.assertEqual(rebel["HP"], 0)

    def test_set_hp_with_positive_int(self):
        set_hp(8)
        self.assertEqual(rebel["HP"], 8)

    def test_set_hp_changed_from_original(self):
        original = rebel["HP"]
        set_hp(4)
        self.assertNotEqual(original, rebel["HP"])
