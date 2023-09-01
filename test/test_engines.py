import unittest
import datetime as dt
from ..engine.engine_type.willoughby_engine import WilloughbyEngine
from ..engine.engine_type.sternman_engine import SternmanEngine
from ..engine.engine_type.capulet_engine import CapuletEngine

class TestWilloughby(unittest.TestCase):

    def test_willoughby_true(self):
        last_service_mileage = 100000
        current_mileage = 190000
        #190000-100000 = 90,000 > 60,000 ..needs service
        s = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(s.needs_service())

    def test_willoughby_false(self):
        last_service_mileage = 100000
        current_mileage = 150000
        # 150000-100000 = 50,000 < 60,000 ..doesn't need service
        s = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(s.needs_service())


class TestSternman(unittest.TestCase):

    def test_sternman_true(self):
        warning_light_is_on = True
        s = SternmanEngine(warning_light_is_on)
        self.assertTrue(s.needs_service())

    def test_sternman_false(self):
        warning_light_is_on = False
        s = SternmanEngine(warning_light_is_on)
        self.assertFalse(s.needs_service())


class TestCapulet(unittest.TestCase):

    def test_capulet_true(self):
        last_service_mileage = 100000
        current_mileage = 140000
        # 140000-100000 = 40,000 > 30,000 ..needs service
        s = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(s.needs_service())

    def test_capulet_false(self):
        last_service_mileage = 100000
        current_mileage = 120000
        # 120000-100000 = 20,000 < 30,000 doesn't need service
        s = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(s.needs_service())

