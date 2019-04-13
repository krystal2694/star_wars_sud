from unittest import TestCase
from q04 import is_all_numbers
from q04 import is_all_strings
from q04 import is_valid_data_structure
from q04 import selection_sort
from q04 import sort_items


class TestIsAllNumbers(TestCase):
    def test_all_numbers_return_type(self):
        self.assertIsInstance(is_all_numbers([-3, 0, 78, 45]), bool)

    def test_is_all_numbers_return_true_with_all_integers(self):
        self.assertTrue(is_all_numbers([-3, 0, 78, 45]))

    def test_is_all_numbers_return_true_with_some_floats(self):
        self.assertTrue(is_all_numbers([-5.5, -3, 0, 3.14, 2]))

    def test_is_all_numbers_return_true_all_floats(self):
        self.assertTrue(is_all_numbers([-2.1, 0.1, -0.9, 5.7]))

    def test_all_numbers_return_false(self):
        self.assertFalse(is_all_numbers([-0.3, '45', 3.14, -80]))


class TestIsAllStrings(TestCase):
    def test_is_all_strings_return_type(self):
        self.assertIsInstance(is_all_strings(['a', 1, '4', 23]), bool)

    def test_is_all_string_yes(self):
        self.assertTrue(is_all_strings(['a', 'the', 'hello', '54']))

    def test_is_all_string_no(self):
        self.assertFalse(is_all_strings(['a', 'the', 'hello', 54]))


class TestSelectionSort(TestCase):
    def test_selection_sort_empty_list(self):
        with self.assertRaises(ValueError):
            selection_sort([])

    def test_selection_sort_non_sortable_items(self):
        with self.assertRaises(ValueError):
            selection_sort(['a', 2, 3.14, 'the'])


class TestSortItems(TestCase):
    def test_sort_items_with_str_items_sorted(self):
        sorted_list = sort_items(0, ['a', 'bee', 'the', 'me', 'car', 'me'])
        for i in range(len(sorted_list) - 1):
            self.assertTrue(sorted_list[i] <= sorted_list[i + 1])

    def test_sort_items_with_numbers_items_sorted(self):
        sorted_list = sort_items(0, [5, 2, 1, 9, 2, 10])
        for i in range(len(sorted_list) - 1):
            self.assertTrue(sorted_list[i] <= sorted_list[i + 1])

    def test_sort_items_return_type(self):
        self.assertIsInstance(sort_items(0, [5, 2, 1, 9, 2, 10]), list)


class TestIsValidDataStructure(TestCase):
    def test_is_valid_data_structure_return_type(self):
        my_list = [['a'], ['the', 2, []], ['bee', 3], ['sdha', 3]]
        self.assertIsInstance(is_valid_data_structure(my_list), bool)

    def test_is_valid_data_structure_with_list_of_different_data_structures(self):
        with self.assertRaises(ValueError):
            my_list = [['a'], ('the', 2, []), ['bee', 3], ['sdha', 3]]
            is_valid_data_structure(my_list)

    def test_is_valid_data_structure_with_list_of_non_sortable_data_structures(self):
        with self.assertRaises(ValueError):
            my_list = [['a'], [2, []], ['bee', 3], [4, 3]]
            is_valid_data_structure(my_list)

    def test_is_valid_data_structure_with_valid_data_structure(self):
        my_list = [['a'], ['the', 2, []], ['bee', 3], ['sdha', 3]]
        self.assertTrue(is_valid_data_structure(my_list))
