import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_area_1(self):
        result = area(7)
        self.assertEqual(result, 49)

    def test_area_2(self):
        result = area(1.7)
        self.assertAlmostEqual(result, 2.89)

    def test_area_3(self):
        result = area(10)
        self.assertAlmostEqual(result, 100)

    def test_perimeter_1(self):
        result = perimeter(0)
        self.assertEqual(result, 0)

    def test_perimeter_2(self):
        result = perimeter(100)
        self.assertEqual(result, 400)

    def test__perimeter_3(self):
        result = perimeter(2.5)
        self.assertAlmostEqual(result, 10)