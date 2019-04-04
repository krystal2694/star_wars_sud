from unittest import TestCase
from student import Student


class TestStudent(TestCase):
    def test_get_average_return_type(self):
        mock_student = Student("Karen", "Perry", "A45312546", False, 65, 50)
        self.assertIsInstance(mock_student.get_average(), float)

    def test_get_average_correct_value(self):
        mock_student = Student("Karen", "Perry", "A45312546", False, 65, 50)
        self.assertEqual(mock_student.get_average(), 57.5)

    def test_get_average_with_student_has_no_grades(self):
        mock_student = Student("Karen", "Perry", "A45312546", False)
        self.assertEqual(mock_student.get_average(), -1)

