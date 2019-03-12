from unittest import TestCase
from unittest.mock import patch
from battle import determine_enemy
from imperial import imperial_forces


class TestDetermineEnemy(TestCase):
    @patch('battle.randint', side_effect=[0, 1, 2, 3, 4, 5, 6])
    def test_enemy_return_type(self, mock_randint):
        for i in range(0, len(imperial_forces)):
            self.assertIsInstance(determine_enemy(), int)

    @patch('battle.randint', side_effect=[0, 1, 2, 3, 4, 5, 6])
    def test_determine_enemy_number_corresponds_randint_result(self, mock_randint):
        for i in range(0, len(imperial_forces)):
            self.assertEqual(determine_enemy(), i)
