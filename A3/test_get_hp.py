from unittest import TestCase
from rebel import get_hp


class TestGetHp(TestCase):
    def test_get_hp_before_game_play(self):
        self.assertEqual(get_hp(), 10)
