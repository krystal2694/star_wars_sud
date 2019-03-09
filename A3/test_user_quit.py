from unittest import TestCase
from sud import user_quit


class TestUserQuit(TestCase):
    def test_user_quit_when_message_is_quit(self):
        with self.assertRaises(SystemExit):
            user_quit("quit")

    def test_user_quit_when_message_is_not_quit(self):
        self.assertEqual(user_quit("Hello"), "Hello")
