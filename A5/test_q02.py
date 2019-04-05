from unittest import TestCase
from q02 import gcd


class TestGcd(TestCase):
    def test_gcd_return_type(self):
        self.assertIsInstance(gcd(120, 45), int)

    def test_gcd_result_is_divisor_of_both_arguments(self):
        result = gcd(120, 45)
        self.assertTrue(120 % result == 0 and 45 % result == 0)

    def test_gcd_with_both_negative_arguments(self):
        self.assertEqual(gcd(-36, -99), -9)

    def test_gcd_with_one_negative_argument(self):
        self.assertEqual(gcd(-184, 98), 2)

    def test_gcd_pass_0_as_argument_a(self):
        with self.assertRaises(ValueError):
            gcd(0, 24)

    def test_gcd_pass_0_as_argument_b(self):
        with self.assertRaises(ValueError):
            gcd(125, 0)

