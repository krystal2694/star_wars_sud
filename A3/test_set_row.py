from unittest import TestCase
from rebel import set_row
from rebel import rebel


class TestSetRow(TestCase):
    def test_set_row(self):
        set_row(4)
        self.assertEqual(rebel["Row"], 4)
