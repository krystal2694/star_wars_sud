from unittest import TestCase
from unittest.mock import patch
from battle import encounter_enemy
from rebel import rebel
import io


class TestEncounterEnemy(TestCase):
    def setUp(self):
        """Reset HP for character before each test."""
        rebel["HP"] = 10

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value="f")
    @patch('battle.randint', side_effect=[5, 10])
    def test_encounter_enemy_with_user_input_f(self, mock_randint, mock_input, mock_stdout):
        expected_output = "\n-------------------------------------------------------------------\n\n" \
                          "Imperial Officer: Prepare to die, rebel scum!!\n\n" \
                          "You strike!\n" \
                          "The Imperial Officer has taken a 5 point hit!\n\n" \
                          "You have defeated the Imperial Officer.\n" \
                          "We are one step closer to peace in the galaxy!\n\n" \
                          "Your HP is 10.\n\n" \
                          "-------------------------------------------------------------------\n\n"
        encounter_enemy(2)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value="r")
    @patch('battle.randint', return_value=3)
    def test_encounter_enemy_with_user_input_r(self, mock_randint, mock_input, mock_stdout):
        expected_output = "\n-------------------------------------------------------------------\n\n"\
                          "You fled the scene unharmed!\n"
        encounter_enemy(1)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["no", "fight", "p", "f"])
    @patch('battle.randint', side_effect=[1, 2, 6, 9, 2, 13, 5, 11])
    def test_encounter_enemy_keep_asking_user_until_input_is_f_or_r(self, mock_randint, mock_input, mock_stdout):
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
        encounter_enemy(4)
        self.assertEqual(expected_output, mock_stdout.getvalue())
