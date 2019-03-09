from unittest import TestCase
from rebel import set_column
from rebel import rebel


class TestSetColumn(TestCase):
    def test_set_column(self):
        set_column(9)
        self.assertEqual(rebel["Column"], 9)
