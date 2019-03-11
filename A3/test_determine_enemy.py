from unittest import TestCase
from unittest.mock import patch
from battle import determine_enemy
from imperial import imperial_forces


class TestDetermineEnemy(TestCase):
    @patch('battle.randint', side_effect=[2, 3, 4, 5, 6])
    def test_determine_enemy_return_none_if_character_does_not_encounter_enemy(self, mock_randint):
        for _ in range(4):
            self.assertIsNone(determine_enemy())

    @patch('battle.randint', side_effect=[1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6])
    def test_enemy_return_int_if_character_encounters_enemy(self, mock_randint):
        for i in range(0, len(imperial_forces)):
            self.assertIsInstance(determine_enemy(), int)

    @patch('battle.randint', side_effect=[1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6])
    def test_determine_enemy_return_number_generated_by_randint(self, mock_randint):
        for i in range(0, len(imperial_forces)):
            self.assertEqual(determine_enemy(), i)
