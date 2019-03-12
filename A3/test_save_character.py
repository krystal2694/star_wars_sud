from unittest import TestCase
from rebel import save_character
from rebel import rebel
import os
import json


class TestSaveCharacter(TestCase):
    # will not work on your computer :(
    def test_save_character_saved_file_exists(self):
        save_character()
        self.assertTrue(os.path.exists("/Users/Krystal/PycharmProjects/A01089672_1510_assignments/A3/player_info.json"))

    def test_save_character_file_can_be_loaded(self):
        save_character()
        filename = "player_info.json"
        with open(filename) as file_object:
            contents = json.load(file_object)
        self.assertTrue(contents)

    def test_save_character_saved_file_contents_same_as_character_info(self):
        save_character()
        filename = "player_info.json"
        with open(filename) as file_object:
            contents = json.load(file_object)
        self.assertEqual(rebel, contents)
