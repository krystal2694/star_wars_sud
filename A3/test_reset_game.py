from unittest import TestCase
from sud import reset_game
from rebel import rebel


class TestResetGame(TestCase):
    def test_reset_game_hp(self):
        rebel["HP"] = 0
        reset_game()
        self.assertEqual(rebel["HP"], 10)

    def test_reset_game_row(self):
        rebel["Row"] = 3
        reset_game()
        self.assertEqual(rebel["Row"], 5)

    def test_reset_game_column(self):
        rebel["Column"] = 7
        reset_game()
        self.assertEqual(rebel["Column"], 5)
