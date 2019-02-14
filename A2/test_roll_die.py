from unittest import TestCase
import dungeonsanddragons


class TestRollDie(TestCase):
    def test_roll_die_with_empty_str(self):
        with self.assertRaises(TypeError):
            dungeonsanddragons.roll_die(1, "")
            dungeonsanddragons.roll_die("", 6)
            dungeonsanddragons.roll_die("", "")

    def test_roll_die_correct_lower_bound(self):
        self.assertTrue(dungeonsanddragons.roll_die(3, 6) >= 3)

    def test_roll_die_correct_higher_bound(self):
        self.assertTrue(dungeonsanddragons.roll_die(3, 6) <= 18)

    def test_roll_die_correct_negative_number_of_rolls(self):
        self.assertTrue(dungeonsanddragons.roll_die(-1, 6) == 0)

    def test_roll_die_correct_negative_number_of_sides(self):
        self.assertTrue(dungeonsanddragons.roll_die(3, -1) == 0)

    def test_roll_die_correct_negative_number_of_rolls_sides(self):
        self.assertTrue(dungeonsanddragons.roll_die(-1, -1) == 0)

    def test_roll_die_output_type(self):
        self.assertIsInstance(dungeonsanddragons.roll_die(3, 6), int)



