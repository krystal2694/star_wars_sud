from unittest import TestCase
import dungeonsanddragons
import string


class TestGenerateName(TestCase):
    def test_choose_generate_name_with_empty_str(self):
        with self.assertRaises(TypeError):
            dungeonsanddragons.generate_name("")

    def test_generate_name_length(self):
        # each syllable contains 2 characters,
        # therefore len(generate_name) should always be syllable * 2
        self.assertEqual(len(dungeonsanddragons.generate_name(3)), 3 * 2)

    def test_create_name_title_case(self):
        name = dungeonsanddragons.generate_name(3)
        self.assertEqual(name[0], name[0].upper())
        self.assertEqual(name[1], name[1].lower())
        self.assertEqual(name[2], name[2].lower())
        self.assertEqual(name[3], name[3].lower())
        self.assertEqual(name[4], name[4].lower())
        self.assertEqual(name[5], name[5].lower())

    def test_create_name_letters(self):
        name = dungeonsanddragons.generate_name(2)
        self.assertIn(name[0], string.ascii_letters)
        self.assertIn(name[1], string.ascii_letters)
        self.assertIn(name[2], string.ascii_letters)
        self.assertIn(name[3], string.ascii_letters)

    def test_create_name_type(self):
        self.assertIsInstance(dungeonsanddragons.generate_name(4), str)
