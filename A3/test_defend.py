from unittest import TestCase
from unittest.mock import patch
from battle import defend
from rebel import rebel
import io


class TestDefend(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.randint', side_effect=[3, 1])
    def test_defend_print_output_when_miss(self, mock_randint, mock_stdout):
        expected_output = "The Imperial Spy strikes!\n" \
                          "You evaded the attack!\n\n"
        defend(4)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.randint', side_effect=[4, 13])
    def test_defend_print_output_when_hit_and_character_survives(self, mock_randint, mock_stdout):
        expected_output = "The Sith Lord strikes!\n" \
                          "You have taken a 4 point hit!\n" \
                          "Your HP has dropped to 6.\n\n"
        rebel["HP"] = 10
        defend(5)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.randint', side_effect=[6, 14])
    def test_defend_print_output_when_hit_and_character_dies(self, mock_randint, mock_stdout):
        expected_output = "The AT-AT Walker strikes!\n" \
                          "You have taken a 6 point hit!\n" \
                          "You have been defeated.\n\n" \
                          "AT-AT Walker: Never underestimate the power of the Dark Side.\n\n"
        rebel["HP"] = 6
        defend(6)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('battle.randint', side_effect=[2, 15])
    def test_defend_when_hit_damage_is_reflected_in_new_hp(self, mock_randint):
        hp_before_attack = rebel["HP"]
        defend(0)
        self.assertEqual(rebel["HP"], hp_before_attack - 2)

    @patch('battle.randint', side_effect=[3, 4])
    def test_defend_when_miss_hp_is_unchanged(self, mock_randint):
        hp_before_attack = rebel["HP"]
        defend(1)
        self.assertEqual(rebel["HP"], hp_before_attack)
