from unittest import TestCase
from unittest.mock import patch
import dungeonsanddragons


class TestFirstAttack(TestCase):
    @patch('dungeonsanddragons.roll_die', side_effect=[15, 5])
    def test_first_attack_opponent_one_goes_first(self, mock_roll_die):
        self.assertTrue(dungeonsanddragons.determine_order())

    @patch('dungeonsanddragons.roll_die', side_effect=[1, 10])
    def test_first_attack_opponent_two_goes_first(self, mock_roll_die):
        self.assertFalse(dungeonsanddragons.determine_order())

    @patch('dungeonsanddragons.roll_die', side_effect=[8, 8, 15, 5])
    def test_first_attack_roll_same_number(self, mock_roll_die):
        self.assertTrue(dungeonsanddragons.determine_order())
