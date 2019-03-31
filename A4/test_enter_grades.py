from unittest import TestCase
from crud import enter_grades
from unittest.mock import patch
import io


class TestEnterGrades(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["89", "78", "85", "done"])
    def test_enter_grades_printed_output(self, mock_input, mock_stdout):
        expected_output = "Enter the student's final grades.\n" \
                          "Enter 'done' when finished or if there are no grades to enter.\n"
        enter_grades()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["89", "78", "85", "done"])
    def test_enter_grades_return_type(self, mock_input):
        self.assertIsInstance(enter_grades(), list)

    @patch('builtins.input', side_effect=["89", "78", "85", "done"])
    def test_enter_grades_elements_in_list_correspond_to_input_values(self, mock_input):
        values_entered = ["89", "78", "85"]
        grades = enter_grades()
        for i in range(len(values_entered)):
            self.assertEqual(grades[i], values_entered[i])

    @patch('builtins.input', side_effect=["89", "78", "85", "done"])
    def test_enter_grades_elements_are_all_digits(self, mock_input):
        for grade in enter_grades():
            self.assertTrue(grade.isdigit())
