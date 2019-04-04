from unittest import TestCase
from q01 import remove_multiples
from q01 import is_prime_number
from q01 import sum_of_primes


class TestRemoveMultiples(TestCase):
    def test_remove_multiples_return_type(self):
        num = 2
        my_list = [2, 3, 4, 5, 6]
        self.assertIsInstance(remove_multiples(num, my_list), list)

    def test_remove_multiples_removes_correct_values(self):
        num = 2
        my_list = [2, 3, 4, 5, 6]
        expected = [2, 3, 5]
        self.assertEqual(remove_multiples(num, my_list), expected)

    def test_remove_multiples_with_negative_ints(self):
        num = -2
        my_list = [-2, -3, -4, -5, -6]
        expected = [-2, -3, -5]
        self.assertEqual(remove_multiples(num, my_list), expected)

    def test_remove_multiples_no_multiples_to_remove(self):
        num = 4
        my_list = [2, 3, 4, 5, 6, 7]
        expected = [2, 3, 4, 5, 6, 7]
        self.assertEqual(remove_multiples(num, my_list), expected)

    def test_remove_multiples_with_empty_list(self):
        num = 4
        my_list = []
        expected = []
        self.assertEqual(remove_multiples(num, my_list), expected)


class TestIsPrimeNumber(TestCase):
    def test_is_prime_number_return_type(self):
        self.assertIsInstance(is_prime_number(5), bool)

    def test_is_prime_number_return_true(self):
        self.assertTrue(is_prime_number(5))

    def test_is_prime_number_return_false(self):
        self.assertFalse(is_prime_number(6))

    def test_is_prime_number_with_negative_num(self):
        self.assertFalse(is_prime_number(-7))


class TestSumOfPrimes(TestCase):
    def test_sum_of_primes_return_type(self):
        self.assertIsInstance(sum_of_primes(11), int)

    def test_sum_of_primes_return_value(self):
        self.assertEqual(sum_of_primes(11), 28)

    def test_sum_of_primes_error(self):
        with self.assertRaises(ValueError):
            sum_of_primes(-1)
