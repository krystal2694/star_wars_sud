from unittest import TestCase
from sud import move_character
from rebel import get_row
from rebel import get_column
# I do not test this function with invalid arguments because an if statement
# in the game loop function already accounts for invalid arguments


class TestMoveCharacter(TestCase):
    def test_move_character_north(self):
        row_before_move = get_row()
        move_character("n")
        self.assertEqual(get_row(), row_before_move - 1)

    def test_move_character_south(self):
        row_before_move = get_row()
        move_character("s")
        self.assertEqual(get_row(), row_before_move + 1)

    def test_move_character_east(self):
        column_before_move = get_column()
        move_character("e")
        self.assertEqual(get_column(), column_before_move + 1)

    def test_move_character_west(self):
        column_before_move = get_column()
        move_character("w")
        self.assertEqual(get_column(), column_before_move - 1)
