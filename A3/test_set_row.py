from unittest import TestCase
from rebel import set_row
from rebel import rebel


class TestSetRow(TestCase):
    def test_set_row_value_reflects_argument_passed(self):
        set_row(4)
        self.assertEqual(rebel["Row"], 4)

    def test_set_row_changed_from_original(self):
        original = rebel["Row"]
        set_row(6)
        self.assertIsNot(original, rebel["Row"])
