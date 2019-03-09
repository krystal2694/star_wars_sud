from unittest import TestCase
from unittest.mock import patch
import rebel
# must run unit tests separately


class TestGetName(TestCase):
    def test_get_name_before_play_enters_name(self):
        self.assertEqual(rebel.rebel["Name"], "")

    @patch('builtins.input', return_value="Han Solo")
    def test_get_name_after_player_enters_name(self, mock_input):
        rebel.set_name()
        self.assertEqual(rebel.rebel["Name"], "Han Solo")
