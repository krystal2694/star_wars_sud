from unittest import TestCase
from rebel import get_hp
import rebel


class TestGetHp(TestCase):
    def test_get_hp_before_game_play(self):
        self.assertIs(get_hp(), rebel.rebel["HP"])

    def test_get_hp_after_modified_hp(self):
        rebel.set_hp(5)
        self.assertIs(get_hp(), rebel.rebel["HP"])

    def test_get_hp_return_type(self):
        self.assertIsInstance(get_hp(), int)
