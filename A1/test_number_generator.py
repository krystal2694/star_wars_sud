from unittest import TestCase
import lotto

lottery_numbers = lotto.number_generator()
lucky_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
              19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
              35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]


class TestNumberGenerator(TestCase):
    def test_number_generator_number_in_list(self):
        self.assertIn(lottery_numbers[0], lucky_list)
        self.assertIn(lottery_numbers[1], lucky_list)
        self.assertIn(lottery_numbers[2], lucky_list)
        self.assertIn(lottery_numbers[3], lucky_list)
        self.assertIn(lottery_numbers[4], lucky_list)
        self.assertIn(lottery_numbers[5], lucky_list)

    def test_number_generator_numbers_unique(self):
        self.assertIsNot(lottery_numbers[0], lottery_numbers[1])
        self.assertIsNot(lottery_numbers[0], lottery_numbers[2])
        self.assertIsNot(lottery_numbers[0], lottery_numbers[3])
        self.assertIsNot(lottery_numbers[0], lottery_numbers[4])
        self.assertIsNot(lottery_numbers[0], lottery_numbers[5])
        self.assertIsNot(lottery_numbers[1], lottery_numbers[2])
        self.assertIsNot(lottery_numbers[1], lottery_numbers[3])
        self.assertIsNot(lottery_numbers[1], lottery_numbers[4])
        self.assertIsNot(lottery_numbers[1], lottery_numbers[5])
        self.assertIsNot(lottery_numbers[2], lottery_numbers[3])
        self.assertIsNot(lottery_numbers[2], lottery_numbers[4])
        self.assertIsNot(lottery_numbers[2], lottery_numbers[5])
        self.assertIsNot(lottery_numbers[3], lottery_numbers[4])
        self.assertIsNot(lottery_numbers[3], lottery_numbers[5])
        self.assertIsNot(lottery_numbers[4], lottery_numbers[5])

    def test_number_generator_numbers_sorted_lowest_to_highest(self):
        self.assertTrue(lottery_numbers[0] < lottery_numbers[1])
        self.assertTrue(lottery_numbers[1] < lottery_numbers[2])
        self.assertTrue(lottery_numbers[2] < lottery_numbers[3])
        self.assertTrue(lottery_numbers[3] < lottery_numbers[4])
        self.assertTrue(lottery_numbers[4] < lottery_numbers[5])

    def test_number_generator_numbers_in_range(self):
        self.assertTrue(1 <= lottery_numbers[0])
        self.assertTrue(1 <= lottery_numbers[1])
        self.assertTrue(1 <= lottery_numbers[2])
        self.assertTrue(1 <= lottery_numbers[3])
        self.assertTrue(1 <= lottery_numbers[4])
        self.assertTrue(1 <= lottery_numbers[5])
        self.assertTrue(49 >= lottery_numbers[0])
        self.assertTrue(49 >= lottery_numbers[1])
        self.assertTrue(49 >= lottery_numbers[2])
        self.assertTrue(49 >= lottery_numbers[3])
        self.assertTrue(49 >= lottery_numbers[4])
        self.assertTrue(49 >= lottery_numbers[5])

    def test_number_generator_length_of_list(self):
        self.assertEqual(len(lottery_numbers), 6)
