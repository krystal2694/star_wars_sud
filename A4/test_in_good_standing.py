from unittest import TestCase
from unittest.mock import patch
from crud import in_good_standing


class TestInGoodStanding(TestCase):
    @patch('builtins.input', return_value="Y")
    def test_in_good_standing_true(self, mock_input):
        self.assertTrue(in_good_standing())

    @patch('builtins.input', return_value="N")
    def test_in_good_standing_false(self, mock_input):
        self.assertFalse(in_good_standing())
