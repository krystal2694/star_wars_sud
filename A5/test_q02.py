from unittest import TestCase
from q02 import gcd
from unittest.mock import patch
import io


class TestGcd(TestCase):
    def test_gcd_return_type(self):
        self.assertIsInstance(gcd(120, 45), int)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gcd_return_with_0(self, mock_stdout):
        expected_output = "a and b have to be non-zero integers.\n"
        gcd(64, 0)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_gcd_result_is_divisor_of_both_arguments(self):
        result = gcd(120, 45)
        self.assertTrue(120 % result == 0 and 45 % result == 0)

    def test_gcd_with_both_negative_arguments(self):
        self.assertEqual(gcd(-36, -99), -9)

    def test_gcd_with_one_negative_argument(self):
        self.assertEqual(gcd(-184, 98), 2)
