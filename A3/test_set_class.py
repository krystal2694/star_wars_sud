from unittest import TestCase
from rebel import set_class
from rebel import rebel


class TestSetClass(TestCase):
    def test_set_class_value_reflects_argument_passed(self):
        set_class("Jedi")
        self.assertEqual(rebel["Class"], "Jedi")

    def test_set_class_changed_from_original(self):
        original = rebel["Class"]
        set_class("Rebel Fighter")
        self.assertIsNot(original, rebel["Class"])
