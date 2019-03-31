from unittest import TestCase
from crud import file_read
from unittest.mock import patch
from unittest.mock import mock_open
from student import Student

mock_file = "Hermione Granger A45875462 True 98 89\n" \
            "Harry Potter A45874512 True 75 86\n"


class TestFileRead(TestCase):
    def test_file_read_return_type(self):
        with patch('builtins.open', mock_open(read_data=mock_file)):
            self.assertIsInstance(file_read(), list)

    def test_file_read_return_list_of_objects(self):
        with patch('builtins.open', mock_open(read_data=mock_file)):
            for student in file_read():
                self.assertIsInstance(student, object)

    def test_file_read_objects_are_class_student(self):
        with patch('builtins.open', mock_open(read_data=mock_file)):
            for student in file_read():
                self.assertIsInstance(student, Student)


