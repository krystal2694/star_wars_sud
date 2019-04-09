from unittest import TestCase
from q03 import check_file, back_up
from unittest.mock import patch, mock_open
import io

mock_backup_file = "Hi, my name is Peter Parker.\n" \
                   "I am the friendly neighbourhood Spiderman.\n" \
                   "I am now a member of the Avengers.\n"


class TestCheckFile(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_file_successful_printed_output(self, mock_stdout):
        with patch('builtins.open', mock_open(read_data=mock_backup_file)):
            mock_contents_list = ["Hi, my name is Peter Parker.\n",
                                  "I am the friendly neighbourhood Spiderman.\n",
                                  "I am now a member of the Avengers.\n"]
            expected_output = "Your file has been backed up successfully.\n"
            check_file(mock_backup_file, mock_contents_list)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_file_failed_printed_output(self, mock_stdout):
        with patch('builtins.open', mock_open(read_data=mock_backup_file)):
            mock_contents_list = ["Hi, my name is Peter Parker.\n",
                                  "I am the friendly neighbourhood Spiderman.\n",
                                  "I am now a member of the Avengers.\n",
                                  "I am in love with a girl name Gwen Stacy"]
            expected_output = "Your file could not be backed up.\n"
            check_file(mock_backup_file, mock_contents_list)
        self.assertEqual(mock_stdout.getvalue(), expected_output)


class TestBackUp(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_back_up_file_not_found_printed_output(self, mock_stdout):
        expected_output = "The file does not exist!\n"
        back_up('file.txt')
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_back_up_file_not_found_return(self):
        self.assertIsNone(back_up('file.txt'))

    # def test_website_file_writes(self):
    #     with patch('builtins.open', mock_open(read_data="")) as mock_file:
    #         mock_file().write.assert_called_once_with('importantFile.txt')
