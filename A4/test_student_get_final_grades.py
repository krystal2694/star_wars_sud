from unittest import TestCase
from student import Student


class TestStudent(TestCase):
    def test_get_final_grades_return_type(self):
        mock_student = Student("Karen", "Perry", "A45312546", "False", "65", "50")
        self.assertIsInstance(mock_student.get_final_grades(), list)

    def test_get_final_grades_return_correct_values(self):
        mock_student = Student("Karen", "Perry", "A45312546", "False", "65", "50")
        self.assertEqual(mock_student.get_final_grades(), ["65", "50"])

    def test_get_final_grades_with_student_has_no_grades(self):
        mock_student = Student("Karen", "Perry", "A45312546", "False")
        self.assertEqual(mock_student.get_final_grades(), [])

