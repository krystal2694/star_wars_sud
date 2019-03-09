from unittest import TestCase
import rebel


class TestSetHp(TestCase):

    def setUp(self):
        rebel.set_hp(10)

    def test_set_hp_0(self):
        rebel.set_hp(0)
        self.assertEqual(rebel.rebel["HP"], 0)
