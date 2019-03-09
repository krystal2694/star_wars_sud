from unittest import TestCase
from rebel import get_row


class TestGetRow(TestCase):
    def test_get_row_before_game_play(self):
        self.assertEqual(get_row(), 5)
