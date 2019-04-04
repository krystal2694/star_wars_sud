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


