from unittest import TestCase
from rebel import set_class
import rebel


class TestSetClass(TestCase):
    def test_set_class_value_reflects_parameter_passed(self):
        set_class("Jedi")
        self.assertEqual(rebel.rebel["Class"], "Jedi")

    def test_set_class_changed_from_original(self):
        original = rebel.rebel["Class"]
        set_class("Rebel Fighter")
        self.assertIsNot(original, rebel.rebel["Class"])
