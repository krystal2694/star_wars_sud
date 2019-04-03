from unittest import TestCase
from student import Student

mock_student = Student("Karen", "Perry", "A45312546", False, 65, 50)


class TestStudent(TestCase):
    def test_get_last_name_return_type(self):
        self.assertIsInstance(mock_student.get_first_name(), str)

    def test_get_last_name_return_correct_value(self):
        self.assertEqual(mock_student.get_last_name(), "Perry")
