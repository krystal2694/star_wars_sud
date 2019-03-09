from unittest import TestCase
from rebel import get_dexterity
import rebel


class TestGetDexterity(TestCase):
    def test_get_dexterity(self):
        self.assertEqual(get_dexterity(), rebel.rebel["Dexterity"])

    def test_get_dexterity_return_type(self):
        self.assertIsInstance(get_dexterity(), int)
