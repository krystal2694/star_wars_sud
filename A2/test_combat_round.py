from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import dungeonsanddragons


class TestCombatRound(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[10, 5, 4, 1, 6, 1])
    def test_attack_miss_miss_both_survive(self, mock_roll_die, mock_stdout):
        bad_fighter = {"Name": "Monoza",
                       "Class": "sorcerer",
                       "HP": 1,
                       "Strength": 12,
                       "Dexterity": 12,
                       "Constitution": 3,
                       "Intelligence": 9,
                       "Wisdom": 9,
                       "Charisma": 18,
                       "XP": 0,
                       "Inventory": ["The Elder Wand"]}
        bad_fighter_2 = {"Name": "Bagiko",
                         "Class": "bard",
                         "HP": 4,
                         "Strength": 12,
                         "Dexterity": 18,
                         "Constitution": 15,
                         "Intelligence": 9,
                         "Wisdom": 6,
                         "Charisma": 9,
                         "XP": 0,
                         "Inventory": ["The Unicorn Horn", "The Belmont Whip"]}
        expected_output = "Monoza goes first:\n" \
                          "Monoza strikes!\n"\
                          "Monoza missed!\n"\
                          "Bagiko's turn:\n"\
                          "Bagiko strikes!\n"\
                          "Bagiko missed!\n"\
                          "End of round --> Monoza's HP is 1. Bagiko's HP is 4.\n"
        dungeonsanddragons.combat_round(bad_fighter, bad_fighter_2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[10, 5, 4, 1, 3, 20])
    def test_attack_miss_hit_both_survive(self, mock_roll_die, mock_stdout):
        bad_fighter = {"Name": "Monoza",
                       "Class": "sorcerer",
                       "HP": 6,
                       "Strength": 12,
                       "Dexterity": 12,
                       "Constitution": 3,
                       "Intelligence": 9,
                       "Wisdom": 9,
                       "Charisma": 18,
                       "XP": 0,
                       "Inventory": ["The Elder Wand"]}
        mediocre_fighter = {"Name": "Bagiko",
                            "Class": "bard",
                            "HP": 4,
                            "Strength": 12,
                            "Dexterity": 18,
                            "Constitution": 15,
                            "Intelligence": 9,
                            "Wisdom": 6,
                            "Charisma": 9,
                            "XP": 0,
                            "Inventory": ["The Unicorn Horn", "The Belmont Whip"]}
        expected_output = "Monoza goes first:\n" \
                          "Monoza strikes!\n"\
                          "Monoza missed!\n"\
                          "Bagiko's turn:\n"\
                          "Bagiko strikes!\n"\
                          "Monoza has taken a 3 point hit!\n"\
                          "Monoza's HP has dropped to 3.\n"\
                          "End of round --> Monoza's HP is 3. Bagiko's HP is 4.\n"
        dungeonsanddragons.combat_round(bad_fighter, mediocre_fighter)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[10, 5, 3, 20, 3, 1])
    def test_attack_hit_miss_both_survive(self, mock_roll_die, mock_stdout):
        bad_fighter = {"Name": "Monoza",
                       "Class": "sorcerer",
                       "HP": 6,
                       "Strength": 12,
                       "Dexterity": 12,
                       "Constitution": 3,
                       "Intelligence": 9,
                       "Wisdom": 9,
                       "Charisma": 18,
                       "XP": 0,
                       "Inventory": ["The Elder Wand"]}
        mediocre_fighter = {"Name": "Bagiko",
                            "Class": "bard",
                            "HP": 4,
                            "Strength": 12,
                            "Dexterity": 18,
                            "Constitution": 15,
                            "Intelligence": 9,
                            "Wisdom": 6,
                            "Charisma": 9,
                            "XP": 0,
                            "Inventory": ["The Unicorn Horn", "The Belmont Whip"]}
        expected_output = "Bagiko goes first:\n" \
                          "Bagiko strikes!\n"\
                          "Monoza has taken a 3 point hit!\n"\
                          "Monoza's HP has dropped to 3.\n"\
                          "Monoza's turn:\n"\
                          "Monoza strikes!\n"\
                          "Monoza missed!\n"\
                          "End of round --> Bagiko's HP is 4. Monoza's HP is 3.\n"
        dungeonsanddragons.combat_round(mediocre_fighter, bad_fighter)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[10, 5, 3, 20, 2, 20])
    def test_attack_hit_hit_both_survive(self, mock_roll_die, mock_stdout):
        mediocre_fighter_2 = {"Name": "Monoza",
                              "Class": "sorcerer",
                              "HP": 6,
                              "Strength": 12,
                              "Dexterity": 12,
                              "Constitution": 3,
                              "Intelligence": 9,
                              "Wisdom": 9,
                              "Charisma": 18,
                              "XP": 0,
                              "Inventory": ["The Elder Wand"]}
        mediocre_fighter = {"Name": "Bagiko",
                            "Class": "bard",
                            "HP": 4,
                            "Strength": 12,
                            "Dexterity": 18,
                            "Constitution": 15,
                            "Intelligence": 9,
                            "Wisdom": 6,
                            "Charisma": 9,
                            "XP": 0,
                            "Inventory": ["The Unicorn Horn", "The Belmont Whip"]}
        expected_output = "Bagiko goes first:\n" \
                          "Bagiko strikes!\n"\
                          "Monoza has taken a 3 point hit!\n"\
                          "Monoza's HP has dropped to 3.\n"\
                          "Monoza's turn:\n"\
                          "Monoza strikes!\n"\
                          "Bagiko has taken a 2 point hit!\n"\
                          "Bagiko's HP has dropped to 2.\n"\
                          "End of round --> Bagiko's HP is 2. Monoza's HP is 3.\n"
        dungeonsanddragons.combat_round(mediocre_fighter, mediocre_fighter_2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[10, 5, 3, 20, 4, 20])
    def test_attack_hit_hit_opponent_one_dies(self, mock_roll_die, mock_stdout):
        good_fighter = {"Name": "Monoza",
                        "Class": "sorcerer",
                        "HP": 6,
                        "Strength": 12,
                        "Dexterity": 12,
                        "Constitution": 3,
                        "Intelligence": 9,
                        "Wisdom": 9,
                        "Charisma": 18,
                        "XP": 0,
                        "Inventory": ["The Elder Wand"]}
        bad_fighter = {"Name": "Bagiko",
                       "Class": "bard",
                       "HP": 4,
                       "Strength": 12,
                       "Dexterity": 18,
                       "Constitution": 15,
                       "Intelligence": 9,
                       "Wisdom": 6,
                       "Charisma": 9,
                       "XP": 0,
                       "Inventory": ["The Unicorn Horn", "The Belmont Whip"]}
        expected_output = "Bagiko goes first:\n" \
                          "Bagiko strikes!\n"\
                          "Monoza has taken a 3 point hit!\n"\
                          "Monoza's HP has dropped to 3.\n"\
                          "Monoza's turn:\n"\
                          "Monoza strikes!\n"\
                          "Bagiko has taken a 4 point hit!\n"\
                          "Bagiko has perished.\n"\
                          "End of round --> Monoza is the winner!\n"
        dungeonsanddragons.combat_round(bad_fighter, good_fighter)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[10, 5, 3, 1, 4, 20])
    def test_attack_miss_hit_opponent_one_dies(self, mock_roll_die, mock_stdout):
        good_fighter = {"Name": "Monoza",
                        "Class": "sorcerer",
                        "HP": 6,
                        "Strength": 12,
                        "Dexterity": 12,
                        "Constitution": 3,
                        "Intelligence": 9,
                        "Wisdom": 9,
                        "Charisma": 18,
                        "XP": 0,
                        "Inventory": ["The Elder Wand"]}
        bad_fighter = {"Name": "Bagiko",
                       "Class": "bard",
                       "HP": 4,
                       "Strength": 12,
                       "Dexterity": 18,
                       "Constitution": 15,
                       "Intelligence": 9,
                       "Wisdom": 6,
                       "Charisma": 9,
                       "XP": 0,
                       "Inventory": ["The Unicorn Horn", "The Belmont Whip"]}
        expected_output = "Bagiko goes first:\n" \
                          "Bagiko strikes!\n"\
                          "Bagiko missed!\n"\
                          "Monoza's turn:\n"\
                          "Monoza strikes!\n"\
                          "Bagiko has taken a 4 point hit!\n"\
                          "Bagiko has perished.\n"\
                          "End of round --> Monoza is the winner!\n"
        dungeonsanddragons.combat_round(bad_fighter, good_fighter)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[10, 5, 6, 20])
    def test_attack_hit_opponent_two_dies(self, mock_roll_die, mock_stdout):
        bad_fighter = {"Name": "Monoza",
                       "Class": "sorcerer",
                       "HP": 6,
                       "Strength": 12,
                       "Dexterity": 12,
                       "Constitution": 3,
                       "Intelligence": 9,
                       "Wisdom": 9,
                       "Charisma": 18,
                       "XP": 0,
                       "Inventory": ["The Elder Wand"]}
        good_fighter = {"Name": "Bagiko",
                        "Class": "bard",
                        "HP": 4,
                        "Strength": 12,
                        "Dexterity": 18,
                        "Constitution": 15,
                        "Intelligence": 9,
                        "Wisdom": 6,
                        "Charisma": 9,
                        "XP": 0,
                        "Inventory": ["The Unicorn Horn", "The Belmont Whip"]}
        expected_output = "Bagiko goes first:\n" \
                          "Bagiko strikes!\n"\
                          "Monoza has taken a 6 point hit!\n"\
                          "Monoza has perished.\n"\
                          "End of round --> Bagiko is the winner!\n"
        dungeonsanddragons.combat_round(good_fighter, bad_fighter)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
