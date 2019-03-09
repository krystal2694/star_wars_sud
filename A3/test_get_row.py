from unittest import TestCase
from rebel import get_row


class TestGetRow(TestCase):
    def test_get_row_before_game_play(self):
        self.assertIs(get_row(), 5)

    def test_get_row_return_type(self):
        self.assertIsInstance(get_row(), int)
