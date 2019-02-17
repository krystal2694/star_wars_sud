from unittest import TestCase
from unittest.mock import patch
import io
import dungeonsanddragons


class TestAttack(TestCase):
    @patch('dungeonsanddragons.roll_die', side_effect=[4, 1])
    def test_attack_miss(self, mock_roll_die):
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
        good_defender = {"Name": "Bagiko",
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
        defender_after_attack = dungeonsanddragons.attack(bad_fighter, good_defender)
        self.assertTrue(good_defender["HP"] == defender_after_attack["HP"])

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[4, 1])
    def test_attack_miss_output(self, mock_roll_die, mock_stdout):
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
        good_defender = {"Name": "Bagiko",
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
        expected_output = "Monoza strikes!\n" \
                          "Monoza missed!\n"
        dungeonsanddragons.attack(bad_fighter, good_defender)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('dungeonsanddragons.roll_die', side_effect=[12, 20])
    def test_attack_hit_defender_dies(self, mock_roll_die):
        good_fighter = {"Name": "Kelabi",
                        "Class": "barbarian",
                        "HP": 10,
                        "Strength": 15,
                        "Dexterity": 12,
                        "Constitution": 6,
                        "Intelligence": 9,
                        "Wisdom": 9,
                        "Charisma": 12,
                        "XP": 0,
                        "Inventory": ["The Sphere of Annihilation"]}
        bad_defender = {"Name": "Helano",
                        "Class": "sorcerer",
                        "HP": 1,
                        "Strength": 9,
                        "Dexterity": 3,
                        "Constitution": 9,
                        "Intelligence": 12,
                        "Wisdom": 12,
                        "Charisma": 8,
                        "XP": 0,
                        "Inventory": ["The Unicorn Horn", "The Belmont Whip"]}
        defender_after_attack = dungeonsanddragons.attack(good_fighter, bad_defender)
        self.assertTrue(defender_after_attack["HP"] <= 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[12, 20])
    def test_attack_hit_defender_dies_output(self, mock_roll_die, mock_stdout):
        good_fighter = {"Name": "Kelabi",
                        "Class": "barbarian",
                        "HP": 10,
                        "Strength": 15,
                        "Dexterity": 12,
                        "Constitution": 6,
                        "Intelligence": 9,
                        "Wisdom": 9,
                        "Charisma": 12,
                        "XP": 0,
                        "Inventory": ["The Sphere of Annihilation"]}
        bad_defender = {"Name": "Helano",
                        "Class": "sorcerer",
                        "HP": 1,
                        "Strength": 9,
                        "Dexterity": 3,
                        "Constitution": 9,
                        "Intelligence": 12,
                        "Wisdom": 12,
                        "Charisma": 8,
                        "XP": 0,
                        "Inventory": ["The Unicorn Horn", "The Belmont Whip"]}
        expected_output = "Kelabi strikes!\n" \
                          "Helano has taken a 12 point hit!\n"\
                          "Helano has perished.\n"\
                          "End of round --> Kelabi is the winner!\n"
        dungeonsanddragons.attack(good_fighter, bad_defender)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('dungeonsanddragons.roll_die', side_effect=[5, 20])
    def test_attack_hit_defender_lives(self, mock_roll_die):
        good_fighter = {"Name": "Kelabi",
                        "Class": "barbarian",
                        "HP": 10,
                        "Strength": 15,
                        "Dexterity": 12,
                        "Constitution": 6,
                        "Intelligence": 9,
                        "Wisdom": 9,
                        "Charisma": 12,
                        "XP": 0,
                        "Inventory": ["The Sphere of Annihilation"]}
        bad_defender = {"Name": "Helano",
                        "Class": "sorcerer",
                        "HP": 6,
                        "Strength": 9,
                        "Dexterity": 10,
                        "Constitution": 9,
                        "Intelligence": 12,
                        "Wisdom": 12,
                        "Charisma": 8,
                        "XP": 0,
                        "Inventory": ["The Unicorn Horn", "The Belmont Whip"]}
        bad_defender_initial_hp = bad_defender["HP"]
        defender_after_attack = dungeonsanddragons.attack(good_fighter, bad_defender)
        self.assertTrue(defender_after_attack["HP"] < bad_defender_initial_hp)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 20])
    def test_attack_hit_defender_lives_output(self, mock_roll_die, mock_stdout):
        good_fighter = {"Name": "Kelabi",
                        "Class": "barbarian",
                        "HP": 10,
                        "Strength": 15,
                        "Dexterity": 12,
                        "Constitution": 6,
                        "Intelligence": 9,
                        "Wisdom": 9,
                        "Charisma": 12,
                        "XP": 0,
                        "Inventory": ["The Sphere of Annihilation"]}
        bad_defender = {"Name": "Helano",
                        "Class": "sorcerer",
                        "HP": 6,
                        "Strength": 9,
                        "Dexterity": 10,
                        "Constitution": 9,
                        "Intelligence": 12,
                        "Wisdom": 12,
                        "Charisma": 8,
                        "XP": 0,
                        "Inventory": ["The Unicorn Horn", "The Belmont Whip"]}
        expected_output = "Kelabi strikes!\n" \
                          "Helano has taken a 5 point hit!\n"\
                          "Helano's HP has dropped to 1.\n"
        dungeonsanddragons.attack(good_fighter, bad_defender)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
