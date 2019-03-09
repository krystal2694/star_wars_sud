from unittest import TestCase
from rebel import set_name
from rebel import rebel
from unittest.mock import patch


class TestSetName(TestCase):
    @patch('builtins.input', return_value="Yoda")
    def test_set_name(self, mock_input):
        set_name()
        self.assertEqual(rebel["Name"], "Yoda")
