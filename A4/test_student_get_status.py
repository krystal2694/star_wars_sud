from unittest import TestCase
from student import Student


class TestStudent(TestCase):
    def test_get_status_return_type(self):
        mock_student = Student("Karen", "Perry", "A45312546", False, 65, 50)
        self.assertIsInstance(mock_student.get_status(), bool)

    def test_get_status_return_correct_value(self):
        mock_student = Student("Karen", "Perry", "A45312546", False, 65, 50)
        self.assertEqual(mock_student.get_status(), False)
