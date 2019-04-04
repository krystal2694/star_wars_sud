from unittest import TestCase
from student import Student
from unittest.mock import patch
import io


class TestStudent(TestCase):
    def test___repr__return_type(self):
        mock_student = Student("Jordan", "Jenkins", "A45687563", True, 89, 91, 85)
        self.assertIsInstance(repr(mock_student), str)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test___repr__return_correct_values(self, mock_stdout):
        mock_student = Student("Jordan", "Jenkins", "A45687563", True, 89, 91, 85)
        expected = "Jordan Jenkins A45687563 True 89 91 85\n"
        print(repr(mock_student))
        self.assertEqual(expected, mock_stdout.getvalue())
