from unittest import TestCase
from unittest.mock import patch
from sud import roll_for_enemy


class TestRollForEnemy(TestCase):
    @patch('sud.randint', return_value=1)
    def test_roll_for_enemy_return_true(self, mock_randint):
        self.assertTrue(roll_for_enemy())

    @patch('sud.randint', return_value=3)
    def test_roll_for_enemy_return_false(self, mock_randint):
        self.assertFalse(roll_for_enemy())

    @patch('sud.randint', return_value=6)
    def test_roll_for_enemy_return_type(self, mock_randint):
        self.assertIsInstance(roll_for_enemy(), bool)
