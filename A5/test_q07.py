from unittest import TestCase
from q07 import is_strong_password


class TestIsStrongPassword(TestCase):
    def test_is_strong_password_return_type(self):
        self.assertIsInstance(is_strong_password("Peanut1234"), bool)

    def test_is_strong_password_with_strong_password(self):
        self.assertTrue(is_strong_password("Peanut1234"))

    def test_is_strong_password_with_password_less_than_8_char(self):
        self.assertFalse(is_strong_password("Peanut1"))

    def test_is_strong_password_with_password_no_uppercase(self):
        self.assertFalse(is_strong_password("peanut1234"))

    def test_is_strong_password_with_password_no_lowercase(self):
        self.assertFalse(is_strong_password("PEANUT1234"))

    def test_is_strong_password_with_password_no_number(self):
        self.assertFalse(is_strong_password("PeanutOne"))

