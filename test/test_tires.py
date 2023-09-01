import unittest
from tire.tire_type.carrigan_tire import CarriganTire
from tire.tire_type.octoprime_tire import OctoprimeTire


class TestCarriganTires(unittest.TestCase):

    def test_carrigan_true(self):
        arr = [0.7,0.9,1,0.9]
        s = CarriganTire(arr)
        self.assertTrue(s.needs_service())

    def test_carrigan_false(self):
        arr = [0.8,0.8,0.8,0.8]
        s = CarriganTire(arr)
        self.assertFalse(s.needs_service())

class TestOctoprimeTires(unittest.TestCase):

    def test_octoprime_true(self):
        arr = [0.7,0.9,1,0.9]
        s = OctoprimeTire(arr)
        self.assertTrue(s.needs_service())

    def test_octoprime_false(self):
        arr = [0.7,0.7,0.7,0.8]
        s = OctoprimeTire(arr)
        self.assertFalse(s.needs_service())