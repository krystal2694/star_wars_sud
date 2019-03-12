from unittest import TestCase
from unittest.mock import patch
from sud import determine_rebel_class
import rebel
import io


class TestDetermineRebelClass(TestCase):
    def setUp(self):
        rebel.rebel["Name"] = "Chris"

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value="1")
    def test_determine_rebel_class_with_choice_knowledge(self, mock_input, mock_stdout):
        expected_output = "\n-------------------------------------------------------------------\n\n"\
                          "Ah! I think you would make a great.. Jedi!\n\n" \
                          "Now, come with me Chris.\n\n"\
                          "We have a galaxy to save!\n\n"\
                          "-------------------------------------------------------------------\n\n"
        determine_rebel_class()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value="2")
    def test_determine_rebel_class_with_choice_strength(self, mock_input, mock_stdout):
        expected_output = "\n-------------------------------------------------------------------\n\n"\
                          "Ah! I think you would make a great.. Rebel Fighter!\n\n" \
                          "Now, come with me Chris.\n\n"\
                          "We have a galaxy to save!\n\n"\
                          "-------------------------------------------------------------------\n\n"
        determine_rebel_class()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value="3")
    def test_determine_rebel_class_with_choice_wit(self, mock_input, mock_stdout):
        expected_output = "\n-------------------------------------------------------------------\n\n"\
                          "Ah! I think you would make a great.. Smuggler!\n\n" \
                          "Now, come with me Chris.\n\n"\
                          "We have a galaxy to save!\n\n"\
                          "-------------------------------------------------------------------\n\n"
        determine_rebel_class()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["12", "two", "g", "1"])
    def test_determine_rebel_class_ask_user_input_until_input_is_valid(self, mock_input, mock_stdout):
        expected_output = "You must choose one from the list above.\n" \
                          "You must choose one from the list above.\n" \
                          "You must choose one from the list above.\n" \
                          "\n-------------------------------------------------------------------\n\n"\
                          "Ah! I think you would make a great.. Jedi!\n\n" \
                          "Now, come with me Chris.\n\n"\
                          "We have a galaxy to save!\n\n"\
                          "-------------------------------------------------------------------\n\n"
        determine_rebel_class()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

