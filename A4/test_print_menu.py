from unittest import TestCase
from unittest.mock import patch
from crud import print_menu
import io


class TestPrintMenu(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_menu_printed_output(self, mock_stdout):
        expected = "--------------------------------------------------\n" \
                   "1. Add student\n" \
                   "2. Delete student\n" \
                   "3. Calculate class average\n" \
                   "4. Print class list\n" \
                   "5. Add grade\n" \
                   "6. Quit\n"
        print_menu()
        self.assertEqual(mock_stdout.getvalue(), expected)
