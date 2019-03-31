from unittest import TestCase
from student import Student

mock_student = Student("Karen", "Perry", "A45312546", "False", "65", "50")


class TestStudent(TestCase):
    def test_get_student_num_return_type(self):
        self.assertIsInstance(mock_student.get_student_num(), str)

    def test_get_student_num_return_correct_value(self):
        self.assertEqual(mock_student.get_student_num(), "A45312546")
