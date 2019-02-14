from unittest import TestCase
import roman_numbers


class TestConvertToRomanNumeral(TestCase):
    def test_convert_to_roman_numeral_smallest_integer(self):
        self.assertEqual("I", roman_numbers.convert_to_roman_numeral(1))

    def test_convert_to_roman_numeral_largest_integer(self):
        self.assertEqual("MMMMMMMMMM", roman_numbers.convert_to_roman_numeral(10000))

    def test_convert_to_roman_numeral_middle_integer(self):
        self.assertEqual("MMMMM", roman_numbers.convert_to_roman_numeral(5000))
