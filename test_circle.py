import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_area_radius(self):
        result = area(1)
        self.assertAlmostEqual(result, math.pi)

    def test_zero_perimeter(self):
        result = perimeter(0)
        self.assertEqual(result, 0)

    def test_perimeter_radius(self):
        result = perimeter(1)
        self.assertAlmostEqual(result, 2 * math.pi)