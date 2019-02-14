from unittest import TestCase
import dungeonsanddragons
import unittest.mock
import io


class TestChooseInventory(TestCase):
    def test_choose_inventory_with_empty_str(self):
        with self.assertRaises(TypeError):
            dungeonsanddragons.choose_inventory([], "")
            dungeonsanddragons.choose_inventory("", 6)
            dungeonsanddragons.choose_inventory("", "")

    def test_choose_inventory_empty_list_selection_0(self):
        self.assertTrue(dungeonsanddragons.choose_inventory([], 0) == [])

    def test_choose_inventory_negative_selection(self):
        inventory = ['a', 'b', 'c', 1, 2, 3]
        self.assertIs(dungeonsanddragons.choose_inventory(inventory, -1), None)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_negative_selection_expected_output(self, mock_stdout):
        inventory = ['a', 'b', 'c', 1, 2, 3]
        expected_output = "Selection must be a positive integer!\n"
        dungeonsanddragons.choose_inventory(inventory, -1)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_choose_inventory_selection_greater_than_inventory_length(self):
        inventory = ['a', 'b', 'c', 1, 2, 3]
        self.assertIs(dungeonsanddragons.choose_inventory(inventory, 7), None)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_selection_greater_than_inventory_length_expected_output(self, mock_stdout):
        inventory = ['a', 'b', 'c', 1, 2, 3]
        expected_output = "Selection is greater than the total number of your inventory!\n"
        dungeonsanddragons.choose_inventory(inventory, 7)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_choose_inventory_selection_equal_to_inventory_length(self):
        inventory = ['b', 'c', 'd', 'a', 'f', 'e']
        self.assertTrue(dungeonsanddragons.choose_inventory(inventory, 6) == ['a', 'b', 'c', 'd', 'e', 'f'])

    def test_choose_inventory_selection_normal(self):
        inventory = ['b', 'c', 'd', 'a', 'f', 'e']
        new_list = dungeonsanddragons.choose_inventory(inventory, 3)
        self.assertIn(new_list[0], inventory)
        self.assertIn(new_list[1], inventory)
        self.assertIn(new_list[2], inventory)

    def test_choose_inventory_type(self):
        inventory = ['a', 'b', 'c', 'd', 'e', 'f']
        self.assertIsInstance(dungeonsanddragons.choose_inventory(inventory, 3), list)
