from unittest import TestCase
import time_calculator


class TestTimeCalculator(TestCase):
    def test_time_calculator_seconds(self):
        self.assertEqual([0, 0, 0, 1], time_calculator.time_calculator(1))

    def test_time_calculator_minutes(self):
        self.assertEqual([0, 0, 1, 0], time_calculator.time_calculator(60))

    def test_time_calculator_hours(self):
        self.assertEqual([0, 1, 0, 0], time_calculator.time_calculator(3600))

    def test_time_calculator_days(self):
        self.assertEqual([1, 0, 0, 0], time_calculator.time_calculator(86400))

    def test_time_calculator_days_hours(self):
        self.assertEqual([1, 1, 0, 0], time_calculator.time_calculator(90000))

    def test_time_calculator_days_hours_minutes(self):
        self.assertEqual([1, 1, 1, 0], time_calculator.time_calculator(90060))

    def test_time_calculator_days_hours_minutes_seconds(self):
        self.assertEqual([1, 1, 1, 1], time_calculator.time_calculator(90061))
