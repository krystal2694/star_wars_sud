from unittest import TestCase
from q09 import decimal_to_base_n
from q09 import base_conversion


class TestDecimalToBaseN(TestCase):
    def test_decimal_to_base_n_return_type(self):
        self.assertIsInstance(decimal_to_base_n(2343, 3), str)

    def test_decimal_to_base_2(self):
        self.assertEqual(decimal_to_base_n(12, 2), "1100")

    def test_decimal_to_base_3(self):
        self.assertEqual(decimal_to_base_n(1212, 3), "1122220")

    def test_decimal_to_base_4(self):
        self.assertEqual(decimal_to_base_n(123, 4), "1323")

    def test_decimal_to_base_5(self):
        self.assertEqual(decimal_to_base_n(124, 5), "444")

    def test_decimal_to_base_6(self):
        self.assertEqual(decimal_to_base_n(542, 6), "2302")

    def test_decimal_to_base_7(self):
        self.assertEqual(decimal_to_base_n(48, 7), "66")

    def test_decimal_to_base_8(self):
        self.assertEqual(decimal_to_base_n(777, 8), "1411")

    def test_decimal_to_base_9(self):
        self.assertEqual(decimal_to_base_n(873, 9), "1170")


class TestBaseConversion(TestCase):
    def test_base_conversion_original_base_lower_than_2(self):
        with self.assertRaises(ValueError):
            base_conversion(-2, 1256, 6)

    def test_base_conversion_original_base_higher_than_10(self):
        with self.assertRaises(ValueError):
            base_conversion(53, 1256, 6)

    def test_base_conversion_destination_base_lower_than_2(self):
        with self.assertRaises(ValueError):
            base_conversion(5, 1256, 1)

    def test_base_conversion_destination_base_higher_than_10(self):
        with self.assertRaises(ValueError):
            base_conversion(5, 1256, 23)

    def test_base_conversion_destination_base_return_type(self):
        self.assertIsInstance(base_conversion(2, 10010, 6), int)

    def test_base_conversion_positive_original_number(self):
        self.assertEqual(base_conversion(4, 1322, 2), 1111010)
