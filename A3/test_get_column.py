from unittest import TestCase
from rebel import get_column
import rebel


class TestGetColumn(TestCase):
    def test_get_column_before_game_play(self):
        self.assertIs(get_column(), rebel.rebel["Column"])

    def test_get_column_after_modified(self):
        rebel.set_column(3)
        self.assertIs(get_column(), rebel.rebel["Column"])

    def test_get_column_return_type(self):
        self.assertIsInstance(get_column(), int)
