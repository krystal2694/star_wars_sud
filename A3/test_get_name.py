from unittest import TestCase
from unittest.mock import patch
from rebel import get_name
import rebel


class TestGetName(TestCase):
    def test_get_name_before_play_enters_name(self):
        self.assertIs(get_name(), rebel.rebel["Name"])

    @patch('builtins.input', return_value="Han Solo")
    def test_get_name_after_player_enters_name(self, mock_input):
        rebel.set_name()
        self.assertEqual(get_name(), "Han Solo")

    def test_get_name_return_type(self):
        self.assertIsInstance(get_name(), str)
