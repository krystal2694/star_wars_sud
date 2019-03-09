from unittest import TestCase
from rebel import set_class
from rebel import rebel


class TestSetClass(TestCase):
    def test_set_class(self):
        set_class("Jedi")
        self.assertEqual(rebel["Class"], "Jedi")
