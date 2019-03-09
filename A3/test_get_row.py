from unittest import TestCase
from rebel import get_row
import rebel


class TestGetRow(TestCase):
    def test_get_row_before_game_play(self):
        self.assertIs(get_row(), rebel.rebel["Row"])

    def test_get_row_after_modified(self):
        rebel.set_row(1)
        self.assertIs(get_row(), rebel.rebel["Row"])

    def test_get_row_return_type(self):
        self.assertIsInstance(get_row(), int)
