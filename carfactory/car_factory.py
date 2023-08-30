from ..engine.engine_type.capulet_engine import CapuletEngine
from ..engine.engine_type.sternman_engine import SternmanEngine
from ..engine.engine_type.willoughby_engine import WilloughbyEngine

from ..battery.battery_type.nubbin_battery import NubbinBattery
from ..battery.battery_type.splinder_battery import SplinderBattery

from ..car import Car

class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = SplinderBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = SplinderBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SplinderBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car