from unittest import TestCase
from sud import heal_character
from rebel import rebel


class TestHealCharacter(TestCase):
    def test_heal_character_when_hp_less_than_10(self):
        for i in range(1, 10):
            rebel["HP"] = i
            self.fail()
