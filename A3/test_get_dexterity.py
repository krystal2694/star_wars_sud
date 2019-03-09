from unittest import TestCase
from rebel import get_dexterity


class TestGetDexterity(TestCase):
    def test_get_dexterity(self):
        self.assertEqual(get_dexterity(), 5)
