from unittest import TestCase
import dungeonsanddragons
import string


class TestGenerateSyllable(TestCase):
    def test_generate_syllable_type(self):
        self.assertIsInstance(dungeonsanddragons.generate_syllable(), str)

    def test_generate_syllable_length(self):
        self.assertEqual(len(dungeonsanddragons.generate_syllable()), 2)

    def test_generate_syllable_is_letter(self):
        self.assertIn(dungeonsanddragons.generate_syllable()[0], string.ascii_letters)
        self.assertIn(dungeonsanddragons.generate_syllable()[1], string.ascii_letters)
