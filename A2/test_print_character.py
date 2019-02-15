from unittest import TestCase
import unittest.mock
import io
import dungeonsanddragons


class TestPrintCharacter(TestCase):
    def test_print_character_with_list(self):
        character = ["Azazi", "bard", 5, 8, 3, 12, 6, 12, 12, 0]
        with self.assertRaises(AttributeError):
            dungeonsanddragons.print_character(character)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_expected_output(self, mock_stdout):
        character = {"Name": "Azazi",
                     "Class": "bard",
                     "HP": 5,
                     "Strength": 18,
                     "Dexterity": 3,
                     "Constitution": 12,
                     "Intelligence": 6,
                     "Wisdom": 12,
                     "Charisma": 12,
                     "XP": 0,
                     "Inventory": []}
        expected_output = "Here is your new character!\n" \
                          "Name: Azazi\n" \
                          "Class: bard\n" \
                          "HP: 5\n" \
                          "Strength: 18\n"\
                          "Dexterity: 3\n" \
                          "Constitution: 12\n"\
                          "Intelligence: 6\n"\
                          "Wisdom: 12\n"\
                          "Charisma: 12\n"\
                          "XP: 0\n"\
                          "Inventory: []\n"
        dungeonsanddragons.print_character(character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_type(self, mock_stdout):
        character = {"Name": "Azazi",
                     "Class": "bard",
                     "HP": 5,
                     "Strength": 18,
                     "Dexterity": 3,
                     "Constitution": 12,
                     "Intelligence": 6,
                     "Wisdom": 12,
                     "Charisma": 12,
                     "XP": 0,
                     "Inventory": []}
        expected_output = "Here is your new character!\n" \
                          "Name: Azazi\n" \
                          "Class: bard\n" \
                          "HP: 5\n" \
                          "Strength: 18\n"\
                          "Dexterity: 3\n" \
                          "Constitution: 12\n"\
                          "Intelligence: 6\n"\
                          "Wisdom: 12\n"\
                          "Charisma: 12\n"\
                          "XP: 0\n"\
                          "Inventory: []\n"
        dungeonsanddragons.print_character(character)
        self.assertIsInstance(mock_stdout.getvalue(), str)
