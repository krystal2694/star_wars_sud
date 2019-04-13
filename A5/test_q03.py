from unittest import TestCase
from q03 import check_file, back_up
from unittest.mock import patch
import io
import os

# create mock file for unit testing purposes
with open('mock_file.txt', 'w') as file_obj:
    file_obj.write("Hi, my name is Peter Parker.\n")
    file_obj.write("I am the friendly neighbourhood Spiderman.\n")
    file_obj.write("I am now a member of the Avengers.\n")


class TestBackUp(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_back_up_file_not_found_printed_output(self, mock_stdout):
        expected_output = "The file does not exist!\n"
        back_up('file.txt')
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_back_up_file_not_found_return(self):
        self.assertIsNone(back_up('file.txt'))

    def test_back_up_file_exists(self):
        back_up('mock_file.txt')
        self.assertTrue(os.path.exists('../A5/mock_file.bak'))

    def test_back_up_file_contents_equal(self):
        back_up('mock_file.txt')

        with open('mock_file.txt') as file_object:
            original_file_content = file_object.readlines()

        with open('mock_file.bak') as file_object:
            back_up_file_content = file_object.readlines()

        self.assertEqual(original_file_content, back_up_file_content)


class TestCheckFile(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_file_successful_printed_output(self, mock_stdout):

        with open('mock_file.txt') as file_object:
            original_file_content = file_object.readlines()

        expected_output = "Generated mock_file.bak\n"
        check_file('mock_file.bak', original_file_content)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_file_failed_printed_output(self, mock_stdout):
        mock_wrong_content = ["Theoren"]
        expected_output = "Your file could not be backed up.\n"
        check_file('mock_file.bak', mock_wrong_content)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

