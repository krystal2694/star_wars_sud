from unittest import TestCase
from unittest.mock import patch
from sud import heal_character
from rebel import rebel
import io


class TestHealCharacter(TestCase):
    def test_heal_character_when_hp_less_than_10(self):
        for i in range(1, 10):
            rebel["HP"] = i
            hp_before_heal = rebel["HP"]
            heal_character()
            self.assertEqual(rebel["HP"], hp_before_heal + 1)

    def test_heal_character_when_hp_less_than_10_print_output(self):
        for i in range(1, 10):
            rebel["HP"] = i
            hp_before_heal = rebel["HP"]
            heal_character()
            self.assertEqual(rebel["HP"], hp_before_heal + 1)

    def test_heal_character_when_at_full_health(self):
        rebel["HP"] = 10
        hp_before_heal = rebel["HP"]
        heal_character()
        self.assertEqual(rebel["HP"], hp_before_heal)


