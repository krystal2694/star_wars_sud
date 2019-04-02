from unittest import TestCase
from crud import delete_student
from unittest import mock
from unittest.mock import patch
import io


original_file = "Wanda Maximoff A7894512 True 85 65 86\n" \
                "Robin Scherbatsky A45214523 True 75 87\n"

file_after_delete = "Wanda Maximoff A7894512 True 85 65 86\n"


class TestDeleteStudent(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value="A12345678")
    def test_delete_student_when_student_num_not_on_file(self, mock_input, mock_stdout):
        with mock.patch('builtins.open', side_effect=[io.StringIO(original_file), io.StringIO(original_file),
                                                      io.StringIO(original_file)]):
            expected_output = "\nThe student number you entered is not on file.\n\n"
            delete_student()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value="A45214523")
    def test_delete_student_successful(self, mock_input, mock_stdout):
        with mock.patch('builtins.open', side_effect=[io.StringIO(original_file), io.StringIO(original_file),
                                                      io.StringIO(original_file), io.StringIO(file_after_delete)]):
            expected_output = "\nStudent successfully deleted.\n\n"
            delete_student()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value="A45214523")
    def test_delete_student_unsuccessful(self, mock_input, mock_stdout):
        with mock.patch('builtins.open', side_effect=[io.StringIO(original_file), io.StringIO(original_file),
                                                      io.StringIO(original_file), io.StringIO(original_file)]):
            expected_output = "\nThe student could not be deleted.\n\n"
            delete_student()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
