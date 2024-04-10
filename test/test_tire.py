import unittest
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wears = [0.4, 0.6, 0.9, 0.3]
        tire = CarriganTire(tire_wears)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wears = [0.4, 0.6, 0.5, 0.3]
        tire = CarriganTire(tire_wears)
        self.assertFalse(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wears = [0.7, 0.6, 0.9, 0.8]
        tire = OctoprimeTire(tire_wears)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wears = [0.7, 0.6, 0.5, 0.7]
        tire = OctoprimeTire(tire_wears)
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()
