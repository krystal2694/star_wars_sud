from unittest import TestCase
from rebel import set_name
from rebel import rebel
from unittest.mock import patch


class TestSetName(TestCase):
    def setUp(self):
        """Reset character name to empty string before each unit test."""
        rebel["Name"] = ""

    @patch('builtins.input', return_value="Yoda")
    def test_set_name_reflects_user_input(self, mock_input):
        set_name()
        self.assertEqual(rebel["Name"], "Yoda")

    @patch('builtins.input', return_value="Chewie")
    def test_set_name_changed_from_original(self, mock_input):
        original = rebel["Name"]
        set_name()
        self.assertIsNot(original, rebel["Name"])
