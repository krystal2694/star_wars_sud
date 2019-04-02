from unittest import TestCase
from crud import print_class_list
from unittest.mock import mock_open
from unittest.mock import patch
import io


class TestPrintClassList(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_class_list(self, mock_stdout):
        mock_file = "Chris Collins A54621542 True 85 68\n" \
                    "Ryan Gosling A01245685 True 87 74\n" \
                    "Chris Evans A04561325 True 85 74\n" \
                    "Tom Holland A01236589 False\n"
        with patch('builtins.open', mock_open(read_data=mock_file)):
            expected_output = "\n--Class List--\n\n" \
                              "Name: Chris Collins, Student Number: A54621542, In Good Standing: True, Grades: 85 68\n" \
                              "Name: Ryan Gosling, Student Number: A01245685, In Good Standing: True, Grades: 87 74\n" \
                              "Name: Chris Evans, Student Number: A04561325, In Good Standing: True, Grades: 85 74\n" \
                              "Name: Tom Holland, Student Number: A01236589, In Good Standing: False, Grades: \n\n\n"
            print_class_list()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
