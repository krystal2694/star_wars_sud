from unittest import TestCase
from crud import file_write
from student import Student
from unittest.mock import mock_open
from unittest.mock import patch


class TestFileWrite(TestCase):
    def test_file_write_successful(self):
        with patch('builtins.open', mock_open(read_data="")) as mock_file:
            mock_student = Student("Bruce", "Banner", "A12145854", "False", "54", "75")
            file_write(mock_student)
            mock_file().write.assert_called_once_with("Bruce Banner A12145854 False 54 75\n")

    def test_file_write_successful_returns_true(self):
        with patch('builtins.open', mock_open(read_data="Bruce Banner A12145854 False 54 75")):
            mock_student = Student("Bruce", "Banner", "A12145854", "False", "54", "75")
            self.assertTrue(file_write(mock_student))

    def test_file_write_return_type(self):
        with patch('builtins.open', mock_open(read_data="Bruce Banner A12145854 False 54 75")):
            mock_student = Student("Bruce", "Banner", "A12145854", "False", "54", "75")
            self.assertIsInstance(file_write(mock_student), bool)
