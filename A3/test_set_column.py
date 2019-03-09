from unittest import TestCase
from rebel import set_column
import rebel


class TestSetColumn(TestCase):
    def test_set_column(self):
        set_column(9)
        self.assertIs(rebel.rebel["Column"], 9)

    def test_set_column_changed_from_original(self):
        original = rebel.get_column()
        set_column(6)
        self.assertIsNot(original, rebel.rebel["Column"])
