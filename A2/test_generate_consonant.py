from unittest import TestCase
import dungeonsanddragons


class TestGenerateConsonant(TestCase):
    def test_generate_consonant_type(self):
        self.assertIsInstance(dungeonsanddragons.generate_consonant(), str)

    def test_generate_consonant_is_consonant(self):
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                      'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        self.assertIn(dungeonsanddragons.generate_consonant(), consonants)

    def test_generate_consonant_length(self):
        self.assertEqual(len(dungeonsanddragons.generate_consonant()), 1)
