import unittest
import datetime as dt
from battery.battery_type.splinder_battery import SplinderBattery
from battery.battery_type.nubbin_battery import NubbinBattery


class TestSplinder(unittest.TestCase):

    def test_splinder_true(self):
        self.lastDate = dt.date(2018,1,1)
        self.currDate = dt.date(2020,1,1)
        s = SplinderBattery(self.lastDate,self.currDate)
        self.assertTrue(s.needs_service())

    def test_splinder_false(self):
        self.lastDate = dt.date(2019,1,1)
        self.currDate = dt.date(2020,1,1)
        s = SplinderBattery(self.lastDate,self.currDate)
        self.assertFalse(s.needs_service())


class TestNubbin(unittest.TestCase):

    def test_nubbin_true(self):
        self.lastDate = dt.date(2016,1,1)
        self.currDate = dt.date(2020,1,1)
        s = NubbinBattery(self.lastDate,self.currDate)
        self.assertTrue(s.needs_service())

    def test_nubbin_false(self):
        self.lastDate = dt.date(2018,1,1)
        self.currDate = dt.date(2020,1,1)
        s = NubbinBattery(self.lastDate,self.currDate)
        self.assertFalse(s.needs_service())