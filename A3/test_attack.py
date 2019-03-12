from unittest import TestCase
from unittest.mock import patch
from battle import attack
from imperial import imperial_forces
import io


class TestAttack(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.randint', side_effect=[1, 3])
    def test_attack_print_output_when_miss(self, mock_randint, mock_stdout):
        expected_output = "You strike!\n" \
                          "The Stormtrooper evaded the attack!\n\n"
        attack(0)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.randint', side_effect=[13, 2])
    def test_attack_print_output_when_hit_and_enemy_survives(self, mock_randint, mock_stdout):
        expected_output = "You strike!\n" \
                          "The Shocktrooper has taken a 2 point hit!\n" \
                          "Their HP has dropped to 3.\n\n"
        attack(1)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.randint', side_effect=[14, 5])
    def test_attack_print_output_when_hit_and_enemy_dies(self, mock_randint, mock_stdout):
        expected_output = "You strike!\n" \
                          "The Imperial Officer has taken a 5 point hit!\n\n" \
                          "You have defeated the Imperial Officer.\n" \
                          "We are one step closer to peace in the galaxy!\n\n"
        attack(2)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('battle.randint', side_effect=[15, 3])
    def test_attack_when_hit_damage_is_reflected_in_new_hp(self, mock_randint):
        hp_before_attack = imperial_forces[3]["HP"]
        attack(3)
        self.assertEqual(imperial_forces[3]["HP"], hp_before_attack - 3)

    @patch('battle.randint', side_effect=[4, 3])
    def test_attack_when_miss_hp_unchanged(self, mock_randint):
        hp_before_attack = imperial_forces[4]["HP"]
        attack(4)
        self.assertEqual(imperial_forces[4]["HP"], hp_before_attack)
