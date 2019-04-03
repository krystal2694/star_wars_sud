from unittest import TestCase
from student import Student


class TestStudent(TestCase):
    def test_add_final_grade_successful(self):
        mock_student = Student("Jenny", "Kramer", "A42154852", True, 89, 76)
        mock_student.add_final_grade(85)
        self.assertEqual(repr(mock_student).split()[4:7], ["89", "76", "85"])

    def test_add_final_grade_with_num_greater_than_100(self):
        mock_student = Student("Jenny", "Kramer", "A42154852", True, 89, 76)
        with self.assertRaises(ValueError):
            mock_student.add_final_grade(150)

    def test_add_final_grade_with_negative_num(self):
        mock_student = Student("Jenny", "Kramer", "A42154852", True, 89, 76)
        with self.assertRaises(ValueError):
            mock_student.add_final_grade(-20)

