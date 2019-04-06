from unittest import TestCase
from q05 import cashmoney


class TestCashMoney(TestCase):
    def test_cashmoney_return_type(self):
        self.assertIsInstance(cashmoney(45.89), dict)

    def test_cashmoney_with_negative_argument(self):
        with self.assertRaises(ValueError):
            cashmoney(-45.89)

    def test_cashmoney_with_non_float(self):
        with self.assertRaises(ValueError):
            cashmoney(128)

    def test_cashmoney_correct_values_in_dict(self):
        self.assertEqual(cashmoney(328.63),
                         {100: 3, 50: 0, 20: 1, 10: 0, 5: 1, 2: 1, 1: 1, 0.25: 2, 0.1: 1, 0.05: 0, 0.01: 2})

    def test_cashmoney_key_hundred(self):
        self.assertEqual(cashmoney(100.00)[100], 1)

    def test_cashmoney_key_fifty(self):
        self.assertEqual(cashmoney(50.00)[50], 1)

    def test_cashmoney_key_twenty(self):
        self.assertEqual(cashmoney(20.00)[20], 1)

    def test_cashmoney_key_ten(self):
        self.assertEqual(cashmoney(10.00)[10], 1)

    def test_cashmoney_key_five(self):
        self.assertEqual(cashmoney(5.00)[5], 1)

    def test_cashmoney_key_toonie(self):
        self.assertEqual(cashmoney(2.00)[2], 1)

    def test_cashmoney_key_loonie(self):
        self.assertEqual(cashmoney(1.00)[1], 1)

    def test_cashmoney_key_quarter(self):
        self.assertEqual(cashmoney(0.25)[0.25], 1)

    def test_cashmoney_key_ten_cents(self):
        self.assertEqual(cashmoney(0.10)[0.10], 1)

    def test_cashmoney_key_five_cents(self):
        self.assertEqual(cashmoney(0.05)[0.05], 1)

    def test_cashmoney_key_cent(self):
        self.assertEqual(cashmoney(0.01)[0.01], 1)
