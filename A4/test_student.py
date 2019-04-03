from unittest import TestCase
from student import Student


class TestStudent(TestCase):
    def test___init__successful_type(self):
        self.assertIsInstance(Student("Jordan", "Jenkins", "A45687563", True, 89, 91, 85), object)

    def test___init__successful_correct_first_name(self):
        mock_student = Student("Jordan", "Jenkins", "A45687563", True, 89, 91, 85)
        self.assertEqual(mock_student.get_first_name(), "Jordan")

    def test___init__successful_correct_last_name(self):
        mock_student = Student("Jordan", "Jenkins", "A45687563", True, 89, 91, 85)
        self.assertEqual(mock_student.get_last_name(), "Jenkins")

    def test___init__successful_correct_student_num(self):
        mock_student = Student("Jordan", "Jenkins", "A45687563", True, 89, 91, 85)
        self.assertEqual(mock_student.get_student_num(), "A45687563")

    def test___init__successful_correct_status(self):
        mock_student = Student("Jordan", "Jenkins", "A45687563", True, 89, 91, 85)
        self.assertEqual(mock_student.get_status(), True)

    def test___init__successful_correct_final_grades(self):
        mock_student = Student("Jordan", "Jenkins", "A45687563", True, 89, 91, 85)
        self.assertEqual(repr(mock_student).split()[4:7], ["89", "91", "85"])

    def test___init__successful_with_no_final_grades(self):
        mock_student = Student("Jordan", "Jenkins", "A45687563", True)
        self.assertEqual(repr(mock_student).split()[4:], [])

    def test___init__with_blank_first_name(self):
        with self.assertRaises(ValueError):
            Student(" ", "Smith", "A45212564", True, 85, 89)

    def test___init__with_non_alpha_first_name(self):
        with self.assertRaises(ValueError):
            Student("K45", "Smith", "A45212564", True, 85, 89)

    def test___init__with_blank_last_name(self):
        with self.assertRaises(ValueError):
            Student("Jane", " ", "A45212564", True, 85, 89)

    def test___init__with_non_alpha_last_name(self):
        with self.assertRaises(ValueError):
            Student("Jane", "S56m", "A45212564", True, 85, 89)

    def test___init__with_student_num_wrong_length(self):
        with self.assertRaises(ValueError):
            Student("Jane", "Smith", "A1234567", True, 85, 89)

    def test___init__with_student_num_not_starting_with_A(self):
        with self.assertRaises(ValueError):
            Student("Jane", "Smith", "b45212564", True, 85, 89)

    def test___init__with_student_num_index_1_to_8_not_all_digits(self):
        with self.assertRaises(ValueError):
            Student("Jane", "Smith", "A4524h4d5", True, 85, 89)

    def test___init__with_grade_greater_than_100(self):
        with self.assertRaises(ValueError):
            Student("Jane", "Smith", "A01024568", True, 85, 109)

    def test___init__with_grade_less_than_0(self):
        with self.assertRaises(ValueError):
            Student("Jane", "Smith", "A01024568", True, -15)

