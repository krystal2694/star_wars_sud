from unittest import TestCase
from crud import add_grade
from unittest import mock
from unittest.mock import patch
import io

mock_file = "Olivia Power A01089672 True 98 85 75\n" \
            "Josh Filafilo A45614582 True 85 78\n"


class TestAddGrade(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["A01089672", "95"])
    def test_add_grade_successful(self, mock_input, mock_stdout):
        with mock.patch('builtins.open', side_effect=[io.StringIO(mock_file), io.StringIO(mock_file),
                                                      io.StringIO(mock_file)]):
            expected_output = "\nGrade successfully added!\n\n"
            add_grade()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["A04521452", "95"])
    def test_add_grade_failed(self, mock_input, mock_stdout):
        with mock.patch('builtins.open', side_effect=[io.StringIO(mock_file), io.StringIO(mock_file),
                                                      io.StringIO(mock_file)]):
            expected_output = "Grade could not be added.\n\n"
            add_grade()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
