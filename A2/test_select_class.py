from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import dungeonsanddragons


class TestSelectClass(TestCase):
    @patch('builtins.input', return_value="1")
    def test_select_class_user_selection_is_returned_barbarian(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), "barbarian")

    @patch('builtins.input', return_value="2")
    def test_select_class_user_selection_is_returned_bard(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), "bard")

    @patch('builtins.input', return_value="3")
    def test_select_class_user_selection_is_returned_cleric(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), "cleric")

    @patch('builtins.input', return_value="4")
    def test_select_class_user_selection_is_returned_druid(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), "druid")

    @patch('builtins.input', return_value="5")
    def test_select_class_user_selection_is_returned_fighter(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), "fighter")

    @patch('builtins.input', return_value="6")
    def test_select_class_user_selection_is_returned_monk(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), "monk")

    @patch('builtins.input', return_value="7")
    def test_select_class_user_selection_is_returned_paladin(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), "paladin")

    @patch('builtins.input', return_value="8")
    def test_select_class_user_selection_is_returned_ranger(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), "ranger")

    @patch('builtins.input', return_value="9")
    def test_select_class_user_selection_is_returned_rogue(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), "rogue")

    @patch('builtins.input', return_value="10")
    def test_select_class_user_selection_is_returned_sorcerer(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), "sorcerer")

    @patch('builtins.input', return_value="11")
    def test_select_class_user_selection_is_returned_warlock(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), "warlock")

    @patch('builtins.input', return_value="12")
    def test_select_class_user_selection_is_returned_wizard(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), "wizard")

    @patch('builtins.input', return_value="6")
    def test_select_class_type(self, mock_input):
        self.assertIsInstance(dungeonsanddragons.select_class(), str)

    @patch('builtins.input', return_value="2")
    def test_select_class_lower_case(self, mock_input):
        self.assertEqual(dungeonsanddragons.select_class(), dungeonsanddragons.select_class().lower())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value="4")
    def test_select_class_expected_output(self, mock_input, mock_stdout):
        expected_output = "------------------------------------------------\n" \
                          "Choose your new character's class by entering the class's corresponding number.\n"\
                          "1 barbarian\n" \
                          "2 bard\n" \
                          "3 cleric\n" \
                          "4 druid\n" \
                          "5 fighter\n" \
                          "6 monk\n" \
                          "7 paladin\n" \
                          "8 ranger\n" \
                          "9 rogue\n" \
                          "10 sorcerer\n" \
                          "11 warlock\n" \
                          "12 wizard\n" \
                          "------------------------------------------------\n"
        dungeonsanddragons.select_class()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
