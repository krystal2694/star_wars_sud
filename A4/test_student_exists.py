from unittest import TestCase
from crud import student_exists
from unittest.mock import patch
from unittest.mock import mock_open


class TestStudentExists(TestCase):
    def test_student_exists_true(self):
        with patch('builtins.open', mock_open(read_data="Krystal Wong A01089672 True")):
            self.assertTrue(student_exists("A01089672"))

    def test_student_exists_false(self):
        with patch('builtins.open', mock_open(read_data="Krystal Wong A01089672 True")):
            self.assertFalse(student_exists("A12547854"))

    def test_student_exists_return_type(self):
        with patch('builtins.open', mock_open(read_data="Krystal Wong A01089672 True")):
            self.assertIsInstance(student_exists("A01089672"), bool)

