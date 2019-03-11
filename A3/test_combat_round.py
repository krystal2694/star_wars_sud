from unittest import TestCase
from unittest.mock import patch
from battle import combat_round
from imperial import imperial_forces
from rebel import rebel
import io


class TestCombatRound(TestCase):
    def setUp(self):
        """Reset HP for character and enemies before each test."""
        rebel["HP"] = 10
        for i in range(len(imperial_forces)):
            imperial_forces[i]["HP"] = 5

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.randint', side_effect=[6, 12])
    def test_combat_round_print_output_enemy_defeated_after_first_attack(self, mock_randint, mock_stdout):
        expected_output = "\n-------------------------------------------------------------------\n\n" \
                          "Imperial Officer: Prepare to die, rebel scum!!\n\n" \
                          "You strike!\n" \
                          "The Imperial Officer has taken a 6 point hit!\n\n" \
                          "You have defeated the Imperial Officer.\n" \
                          "We are one step closer to peace in the galaxy!\n\n" \
                          "Your HP is 10.\n\n" \
                          "-------------------------------------------------------------------\n\n"
        combat_round(2)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.randint', side_effect=[2, 12, 3, 8, 3, 9])
    def test_combat_round_print_output_enemy_retaliates_if_they_survive_first_attack(self, mock_randint, mock_stdout):
        expected_output = "\n-------------------------------------------------------------------\n\n" \
                          "Bounty Hunter: Prepare to die, rebel scum!!\n\n" \
                          "You strike!\n" \
                          "The Bounty Hunter has taken a 2 point hit!\n" \
                          "Their HP has dropped to 3.\n\n" \
                          "The Bounty Hunter strikes!\n" \
                          "You have taken a 3 point hit!\n" \
                          "Your HP has dropped to 7.\n\n" \
                          "You strike!\n" \
                          "The Bounty Hunter has taken a 3 point hit!\n\n" \
                          "You have defeated the Bounty Hunter.\n" \
                          "We are one step closer to peace in the galaxy!\n\n" \
                          "Your HP is 7.\n\n" \
                          "-------------------------------------------------------------------\n\n"
        combat_round(3)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.randint', side_effect=[1, 2, 6, 9, 2, 13, 5, 11])
    def test_combat_round_print_output_round_continues_until_someone_defeated(self, mock_randint, mock_stdout):
        expected_output = "\n-------------------------------------------------------------------\n\n" \
                          "Imperial Spy: Prepare to die, rebel scum!!\n\n" \
                          "You strike!\n" \
                          "The Imperial Spy evaded the attack!\n\n" \
                          "The Imperial Spy strikes!\n" \
                          "You have taken a 6 point hit!\n" \
                          "Your HP has dropped to 4.\n\n" \
                          "You strike!\n" \
                          "The Imperial Spy has taken a 2 point hit!\n" \
                          "Their HP has dropped to 3.\n\n" \
                          "The Imperial Spy strikes!\n" \
                          "You have taken a 5 point hit!\n" \
                          "You have been defeated.\n\n" \
                          "Imperial Spy: Never underestimate the power of the Dark Side.\n\n"
        combat_round(4)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('battle.randint', side_effect=[1, 2, 6, 9, 2, 13, 5, 11])
    def test_combat_round_enemy_hp_reset_to_5_at_end_of_round(self, mock_randint):
        for i in range(len(imperial_forces)):
            combat_round(i)
            self.assertEqual(imperial_forces[i]["HP"], 5)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.randint', side_effect=[5, 9])
    def test_combat_round_print_output_print_character_HP_at_end_of_round(self, mock_randint, mock_stdout):
        character_hp_statement = "Your HP is 10.\n\n"
        combat_round(1)
        self.assertIn(character_hp_statement, mock_stdout.getvalue())
