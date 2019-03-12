from unittest import TestCase
from unittest.mock import patch
from sud import roll_for_enemy


class TestRollForEnemy(TestCase):
    @patch('sud.randint', return_value=1)
    def test_roll_for_enemy_with_int_1(self, mock_randint):
        self.assertTrue(roll_for_enemy())

    @patch('sud.randint', return_value=2)
    def test_roll_for_enemy_with_int_2(self, mock_randint):
        self.assertFalse(roll_for_enemy())

    @patch('sud.randint', return_value=3)
    def test_roll_for_enemy_with_int_3(self, mock_randint):
        self.assertFalse(roll_for_enemy())

    @patch('sud.randint', return_value=4)
    def test_roll_for_enemy_with_int_4(self, mock_randint):
        self.assertFalse(roll_for_enemy())

    @patch('sud.randint', return_value=5)
    def test_roll_for_enemy_with_int_5(self, mock_randint):
        self.assertFalse(roll_for_enemy())

    @patch('sud.randint', return_value=6)
    def test_roll_for_enemy_with_int_6(self, mock_randint):
        self.assertFalse(roll_for_enemy())


