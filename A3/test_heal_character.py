from unittest import TestCase
from unittest.mock import patch
from sud import heal_character
from rebel import rebel
import io


class TestHealCharacter(TestCase):
    def test_heal_character_when_hp_less_than_10(self):
        for i in range(1, 10):
            rebel["HP"] = i
            hp_before_heal = rebel["HP"]
            heal_character()
            self.assertEqual(rebel["HP"], hp_before_heal + 1)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_heal_character_when_hp_less_than_10_print_output(self, mock_stdout):
        for i in range(1, 10):
            rebel["HP"] = i
            heal_character()
        expected_output = "You're healing! Your HP is 2.\n" \
                          "You're healing! Your HP is 3.\n" \
                          "You're healing! Your HP is 4.\n" \
                          "You're healing! Your HP is 5.\n" \
                          "You're healing! Your HP is 6.\n" \
                          "You're healing! Your HP is 7.\n" \
                          "You're healing! Your HP is 8.\n" \
                          "You're healing! Your HP is 9.\n" \
                          "You're healing! Your HP is 10.\n"
        self.assertEqual(expected_output, mock_stdout.getvalue())

    def test_heal_character_when_hp_is_10(self):
        # does not increase hp when character already at full health
        rebel["HP"] = 10
        hp_before_heal = rebel["HP"]
        heal_character()
        self.assertEqual(rebel["HP"], hp_before_heal)
