from unittest import TestCase
from crud import calculate_class_average
from unittest.mock import mock_open
from unittest.mock import patch


class TestCalculateClassAverage(TestCase):
    def test_calculate_class_average_return_type(self):
        mock_file = "Chris Hemsworth A54621542 True 85 68 94\n" \
                    "Ryan Gosling A01245685 True 87 74\n" \
                    "Chris Evans A04561325 True 85 74 82\n" \
                    "Tom Holland A01236589 False\n"
        with patch('builtins.open', mock_open(read_data=mock_file)):
            self.assertIsInstance(calculate_class_average(), float)

    def test_calculate_class_average_correct_value(self):
        mock_file = "Chris Hemsworth A54621542 True 100 50\n" \
                    "Ryan Gosling A01245685 True 90\n"
        with patch('builtins.open', mock_open(read_data=mock_file)):
            self.assertEqual(calculate_class_average(), 82.50)

    def test_calculate_class_average_exclude_students_with_no_grades(self):
        mock_file = "Chris Hemsworth A54621542 True 100 50\n" \
                    "Ryan Gosling A01245685 True\n"
        with patch('builtins.open', mock_open(read_data=mock_file)):
            self.assertEqual(calculate_class_average(), 75.00)
