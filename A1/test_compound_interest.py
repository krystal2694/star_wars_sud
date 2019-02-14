from unittest import TestCase
import compound_interest


class TestCompoundInterest(TestCase):
    def test_compound_interest_principal_small_float(self):
        self.assertEqual(2.061031562164711e-05, compound_interest.compound_interest(0.00001, 0.15, 2, 5))

    def test_compound_interest__principal_medium_float(self):
        self.assertEqual(103051.57810823555, compound_interest.compound_interest(50000.0, 0.15, 2, 5))

    def test_compound_interest_principal_large_float(self):
        self.assertEqual(162889.4626777442, compound_interest.compound_interest(100000.0, 0.10, 2, 5))

    def test_compound_interest_annual_interest_small_float(self):
        self.assertEqual(1000.0500011250153, compound_interest.compound_interest(1000.0, 0.00001, 2, 5))

    def test_compound_interest__annual_interest_medium_float(self):
        self.assertEqual(9313.225746154785, compound_interest.compound_interest(1000.0, 0.5, 2, 5))

    def test_compound_interest_annual_interest_absurdly_large_float(self):
        self.assertEqual(1.1046221254112045e+23, compound_interest.compound_interest(1000.0, 200.0, 2, 5))

    def test_compound_interest_compound_small_positive_integer(self):
        self.assertEqual(2011.3571874999993, compound_interest.compound_interest(1000.0, 0.15, 1, 5))

    def test_compound_interest_compound_middle_positive_integer(self):
        self.assertEqual(2116.7619151231984, compound_interest.compound_interest(1000.0, 0.15, 500, 5))

    def test_compound_interest_compound_large_positive_integer(self):
        self.assertEqual(2116.8809506179537, compound_interest.compound_interest(1000.0, 0.15, 1000, 5))

    def test_compound_interest_years_small_positive_integer(self):
        self.assertEqual(1155.625, compound_interest.compound_interest(1000.0, 0.15, 2, 1))

    def test_compound_interest_years_middle_positive_integer(self):
        self.assertEqual(1383077.2099250783, compound_interest.compound_interest(1000.0, 0.15, 2, 50))

    def test_compound_interest_years_large_positive_integer(self):
        self.assertEqual(1912902568.614139, compound_interest.compound_interest(1000.0, 0.15, 2, 100))

    def test_compound_interest_years_small_positive_float(self):
        self.assertEqual(1014.5692440496563, compound_interest.compound_interest(1000.0, 0.15, 2, 0.1))

    def test_compound_interest_years_middle_positive_float(self):
        self.assertEqual(1486808.000669459, compound_interest.compound_interest(1000.0, 0.15, 2, 50.5))

    def test_compound_interest_years_large_positive_float(self):
        self.assertEqual(2147565374.356965, compound_interest.compound_interest(1000.0, 0.15, 2, 100.8))
