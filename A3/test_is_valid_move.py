from unittest import TestCase
from sud import is_valid_move
from rebel import set_row
from rebel import set_column
# I do not test this function with invalid arguments because an if statement
# in the game loop function already accounts for invalid arguments


class TestIsValidMove(TestCase):
    def test_is_valid_move_with_north_valid_move(self):
        for i in range(1, 10):
            set_row(i)
            self.assertTrue(is_valid_move("n"))

    def test_is_valid_move_with_north_invalid_move(self):
        set_row(0)
        self.assertFalse(is_valid_move("n"))

    def test_is_valid_move_with_south_valid_move(self):
        for i in range(0, 9):
            set_row(i)
            self.assertTrue(is_valid_move("s"))

    def test_is_valid_move_with_south_invalid_move(self):
        set_row(10)
        self.assertFalse(is_valid_move("s"))

    def test_is_valid_move_with_east_valid_move(self):
        for i in range(0, 9):
            set_column(i)
            self.assertTrue(is_valid_move("e"))

    def test_is_valid_move_with_east_invalid_move(self):
        set_column(10)
        self.assertFalse(is_valid_move("e"))

    def test_is_valid_move_with_west_valid_move(self):
        for i in range(1, 10):
            set_column(i)
            self.assertTrue(is_valid_move("w"))

    def test_is_valid_move_with_west_invalid_move(self):
        set_column(0)
        self.assertFalse(is_valid_move("w"))
