from unittest import TestCase
from rebel import set_column
from rebel import rebel


class TestSetColumn(TestCase):
    def test_set_column_value_reflects_parameter_passed(self):
        set_column(9)
        self.assertIs(rebel["Column"], 9)

    def test_set_column_changed_from_original(self):
        original = rebel["Column"]
        set_column(6)
        self.assertIsNot(original, rebel["Column"])
