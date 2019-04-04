from unittest import TestCase
from student import Student


class TestStudent(TestCase):
    def test_get_first_name_return_type(self):
        mock_student = Student("Karen", "Perry", "A45312546", False, 65, 50)
        self.assertIsInstance(mock_student.get_first_name(), str)

    def test_get_first_name_return_correct_value(self):
        mock_student = Student("Karen", "Perry", "A45312546", False, 65, 50)
        self.assertEqual(mock_student.get_first_name(), "Karen")
