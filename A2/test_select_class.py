from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import dungeonsanddragons


class TestSelectClass(TestCase):
    @patch('builtins.input', return_value="cleric")
    def test_select_class_user_selection_is_returned(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), "cleric")

    @patch('builtins.input', return_value="wizard")
    def test_select_class_type(self, mock_input):
        self.assertIsInstance(dungeonsanddragons.select_class(), str)

    @patch('builtins.input', return_value="barbarian")
    def test_select_class_lower_case(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), dungeonsanddragons.select_class().lower())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value="fighter")
    def test_select_class_expected_output(self, mock_input, mock_stdout):
        expected_output = "------------------------------------------------\n" \
                          "Choose your new character's class from the following list.\n" \
                          "['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', " \
                          "'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']\n"
        dungeonsanddragons.select_class()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
