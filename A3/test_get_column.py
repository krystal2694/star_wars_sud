from unittest import TestCase
from rebel import get_column


class TestGetColumn(TestCase):
    def test_get_column_before_game_play(self):
        self.assertEqual(get_column(), 5)
