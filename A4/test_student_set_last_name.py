from unittest import TestCase
from student import Student


class TestStudent(TestCase):
    def test_set_last_name_with_blank_last_name(self):
        mock_student = Student("Jenny", "Kramer", "A42154852", "True", "89", "76")
        with self.assertRaises(ValueError):
            mock_student.set_last_name(" ")

    def test_set_last_name_with_non_alpha(self):
        mock_student = Student("Jenny", "Kramer", "A42154852", "True", "89", "76")
        with self.assertRaises(ValueError):
            mock_student.set_last_name("J8k")

    def test_set_last_name_corresponds_to_input(self):
        mock_student = Student("Jenny", "Kramer", "A42154852", "True", "89", "76")
        mock_student.set_last_name("Farrell")
        self.assertEqual(mock_student.get_last_name(), "Farrell")
