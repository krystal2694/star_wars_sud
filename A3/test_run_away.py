from unittest import TestCase
from unittest.mock import patch
from battle import run_away
from rebel import rebel
import io


class TestRunAway(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.randint', return_value=3)
    def test_run_away_successful_print_output(self, mock_randint, mock_stdout):
        expected_output = "\n-------------------------------------------------------------------\n\n"\
                          "You fled the scene unharmed!\n"
        run_away(1)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.randint', side_effect=[1, 4])
    def test_run_away_unsuccessful_print_output(self, mock_randint, mock_stdout):
        expected_output = "\n-------------------------------------------------------------------\n\n"\
                          "The Sith Lord struck you as you fled!\n\n" \
                          "You have taken a 4 point hit, your HP is 6.\n"
        run_away(5)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('battle.randint', side_effect=[1, 2])
    def test_run_away_unsuccessful_character_hp_modified(self, mock_randint):
        hp_before_damage = rebel["HP"]
        run_away(4)
        self.assertEqual(rebel["HP"], hp_before_damage - 2)


