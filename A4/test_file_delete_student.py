from unittest import TestCase
from crud import file_delete_student
from unittest import mock
from unittest.mock import patch
import io

original_file = "Wanda Maximoff A7894512 True 85 65 86\n" \
                "Robin Scherbatsky A45214523 True 75 87\n"

file_after_delete = "Wanda Maximoff A7894512 True 85 65 86\n"


class TestFileDeleteStudent(TestCase):
    def test_file_delete_student_successful(self):
        with mock.patch('builtins.open', side_effect=[io.StringIO(original_file), io.StringIO(original_file),
                                                      io.StringIO(file_after_delete)]):
            self.assertTrue(file_delete_student("A45214523"))

    def test_file_delete_student_failed(self):
        with mock.patch('builtins.open', side_effect=[io.StringIO(original_file), io.StringIO(original_file),
                                                      io.StringIO(original_file)]):
            self.assertFalse(file_delete_student("A45214523"))
