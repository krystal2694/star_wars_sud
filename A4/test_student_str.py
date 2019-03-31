from unittest import TestCase
from student import Student
from unittest.mock import patch
import io

mock_student = Student("Jordan", "Jenkins", "A45687563", "True", "89", "91", "85")


class TestStudent(TestCase):
    # not sure about this one, ask Chris
    def test___str__return_type(self):
        self.assertIsInstance(str(mock_student), str)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test___str__return_correct_values(self, mock_stdout):
        expected = "Jordan Jenkins A45687563 True 89 91 85\n"
        print(mock_student)
        self.assertEqual(expected, mock_stdout.getvalue())