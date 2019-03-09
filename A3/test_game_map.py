from unittest import TestCase
from unittest.mock import patch
from sud import game_map
import io


class TestGameMap(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_map_print_output(self, mock_stdout):
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
        game_map()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
