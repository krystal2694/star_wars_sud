from unittest import TestCase
from student import Student

mock_student = Student("Karen", "Perry", "A45312546", "False", "65", "50")


class TestStudent(TestCase):
    def test_get_status_return_type(self):
        self.assertIsInstance(mock_student.get_status(), str)

    def test_get_status_return_correct_value(self):
        self.assertEqual(mock_student.get_status(), "False")
