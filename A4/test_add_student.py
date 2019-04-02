from unittest import TestCase
from crud import add_student
from unittest import mock
from unittest.mock import patch
import io

original_file = "Rob Stark A47585945 True 95 78"

file_after_add = "Rob Stark A47585945 True 95 78\n" \
                 "Jon Snow A01024575 True 87 98\n"


class TestAddStudent(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_student_successful_print_output(self, mock_stdout):
        with mock.patch('builtins.open', side_effect=[io.StringIO(original_file), io.StringIO(original_file),
                                                      io.StringIO(file_after_add)]):
            mock_student_info = ["Jon", "Snow", "A01024575", "True", ["87", "98"]]
            expected_output = "\nStudent successfully added:\n" \
                              "Name: Jon Snow, Student Number: A01024575, In Good Standing: True, Grades: 87 98\n\n"
            add_student(mock_student_info)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_student_print_output_when_student_already_exists_in_system(self, mock_stdout):
        with mock.patch('builtins.open', return_value=io.StringIO(original_file)):
            mock_student_info = ["Rob", "Stark", "A47585945", "True", ["95", "78"]]
            expected_output = "\nThe student number you entered already exists in the system!\n\n"
            add_student(mock_student_info)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_student_print_output_when_file_write_was_unsuccessful(self, mock_stdout):
        with mock.patch('builtins.open', side_effect=[io.StringIO(original_file), io.StringIO(original_file),
                                                      io.StringIO(original_file)]):
            mock_student_info = ["Jon", "Snow", "A01024575", "True", ["87", "98"]]
            expected_output = "\nStudent could not be written to file.\n\n"
            add_student(mock_student_info)
            self.assertEqual(mock_stdout.getvalue(), expected_output)
