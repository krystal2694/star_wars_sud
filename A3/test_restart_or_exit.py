from unittest import TestCase
from unittest.mock import patch
from sud import restart_or_exit
from rebel import rebel
import io


class TestRestartOrExit(TestCase):
    # set hp to 0 for each unit test so the function asks the user if they would like to play again
    def setUp(self):
        rebel["HP"] = 0

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["w", "3", "no", "y"])
    def test_restart_or_exit_ask_user_input_until_input_is_valid(self, mock_input, mock_stdout):
        expected_output = "\n" \
                          "✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ \n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                ⛒               ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ \n\n"
        restart_or_exit()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value="y")
    def test_restart_or_exit_with_user_input_y(self, mock_input, mock_stdout):
        expected_output = "\n" \
                          "✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ \n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                ⛒               ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨                                 ✨\n" \
                          "✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ \n\n"
        restart_or_exit()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', return_value="n")
    def test_restart_or_exit_with_user_input_n(self, mock_input):
        with self.assertRaises(SystemExit):
            restart_or_exit()
