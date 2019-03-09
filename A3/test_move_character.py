from unittest import TestCase
from sud import move_character
from rebel import rebel
# I do not test this function with invalid arguments because an if statement
# in the game loop function already accounts for invalid arguments


class TestMoveCharacter(TestCase):
    def test_move_character_north(self):
        row_before_move = rebel["Row"]
        move_character("n")
        self.assertEqual(rebel["Row"], row_before_move - 1)

    def test_move_character_south(self):
        row_before_move = rebel["Row"]
        move_character("s")
        self.assertEqual(rebel["Row"], row_before_move + 1)

    def test_move_character_east(self):
        column_before_move = rebel["Column"]
        move_character("e")
        self.assertEqual(rebel["Column"], column_before_move + 1)

    def test_move_character_west(self):
        column_before_move = rebel["Column"]
        move_character("w")
        self.assertEqual(rebel["Column"], column_before_move - 1)
