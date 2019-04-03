from unittest import TestCase
from unittest.mock import patch
from student import Student
from crud import add_grade_to_student
import io


class TestAddGradeToStudent(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_grade_to_student_print_output(self, mock_stdout):
        mock_student = Student("Riley", "Cooper", "A25478541", True, 85)
        add_grade_to_student(mock_student, 86)
        expected_output = "\nGrade successfully added!\n\n"
        self.assertEqual(expected_output, mock_stdout.getvalue())

