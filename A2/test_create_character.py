from unittest import TestCase
from unittest.mock import patch
import unittest
import io
import dungeonsanddragons


class TestCreateCharacter(TestCase):
    def test_create_character_with_empty_str(self):
        with self.assertRaises(TypeError):
            dungeonsanddragons.create_character("")

    @patch('dungeonsanddragons.select_class', return_valuet="fighter")
    def test_create_character_type(self, mock_select_class):
        self.assertIsInstance(dungeonsanddragons.create_character(3), dict)

    @patch('dungeonsanddragons.select_class', return_valuet="ranger")
    def test_create_character_syllable_0(self, mock_select_class):
        self.assertEqual(dungeonsanddragons.create_character(0), None)

    @patch('dungeonsanddragons.select_class', return_value="wizard")
    def test_create_character_syllable_less_than_0(self, mock_select_class):
        self.assertEqual(dungeonsanddragons.create_character(-2), None)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.select_class', return_valuet="paladin")
    def test_create_character_syllable_less_or_equal_0_expected_output(self, mock_select_class, mock_stdout):
        expected_output = "syllables must be a positive integer!\n"
        dungeonsanddragons.create_character(-4)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('dungeonsanddragons.select_class', return_value="bard")
    def test_create_character_correct_keys(self, mock_select_class):
        character = dungeonsanddragons.create_character(2)
        character_keys = ["Name", "Class", "HP", "Strength", "Dexterity", "Constitution",
                          "Intelligence", "Wisdom", "Charisma", "XP", "Inventory"]
        for key in character.keys():
            self.assertIn(key, character_keys)
