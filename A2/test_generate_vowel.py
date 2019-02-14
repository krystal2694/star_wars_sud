from unittest import TestCase
import dungeonsanddragons


class TestGenerateVowel(TestCase):
    def test_generate_vowel_type(self):
        self.assertIsInstance(dungeonsanddragons.generate_vowel(), str)

    def test_generate_vowel_is_vowel(self):
        vowels = ["a", "e", "i", "o", "u", "y"]
        self.assertIn(dungeonsanddragons.generate_vowel(), vowels)

    def test_generate_vowel_length(self):
        self.assertEqual(len(dungeonsanddragons.generate_vowel()), 1)
