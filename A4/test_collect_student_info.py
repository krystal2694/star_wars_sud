from unittest import TestCase
from unittest.mock import patch
from crud import collect_student_info
import io


class TestCollectStudentInfo(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["Peter", "Parker", "A21487956", "Y", "85", "done"])
    def test_collect_student_info_printed_output(self, mock_input, mock_stdout):
        expected = "\nPlease enter the students' information.\n" \
                   "Enter the student's final grades.\n" \
                   "Enter 'done' when finished or if there are no grades to enter.\n"
        collect_student_info()
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('builtins.input', side_effect=["Peter", "Parker", "A21487956", "Y", "85", "done"])
    def test_collect_student_info_return_type(self, mock_input):
        self.assertIsInstance(collect_student_info(), list)

    @patch('builtins.input', side_effect=["Peter", "Parker", "A21487956", "Y", "85", "done"])
    def test_collect_student_info_values_reflect_user_input(self, mock_input):
        user_input = ["Peter", "Parker", "A21487956", True, [85]]
        student_info = collect_student_info()
        for i in range(len(user_input)):
            self.assertEqual(user_input[i], student_info[i])
