from unittest import TestCase
from sud import reset_game
from rebel import rebel


class TestResetGame(TestCase):
    def test_reset_game_hp_reset_to_10(self):
        rebel["HP"] = 0
        reset_game()
        self.assertEqual(rebel["HP"], 10)

    def test_reset_game_row_reset_to_5(self):
        rebel["Row"] = 3
        reset_game()
        self.assertEqual(rebel["Row"], 5)

    def test_reset_game_column_reset_to_10(self):
        rebel["Column"] = 7
        reset_game()
        self.assertEqual(rebel["Column"], 5)
