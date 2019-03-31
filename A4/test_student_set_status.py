from unittest import TestCase
from student import Student


class TestStudent(TestCase):
    def test_set_status_reflects_argument_passed(self):
        mock_student = Student("Jenny", "Kramer", "A42154852", "True", "89", "76")
        mock_student.set_status("False")
        self.assertEqual(mock_student.get_status(), "False")

    def test_set_status_with_invalid_value(self):
        mock_student = Student("Jenny", "Kramer", "A42154852", "True", "89", "76")
        with self.assertRaises(ValueError):
            mock_student.set_status("Good")
