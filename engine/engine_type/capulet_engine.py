from engine.engine import Engine

class CapuletEngine(Engine):
    def __init__(self,last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.willoughby_milage_need_service = 30000

    def needs_service(self):
        if(self.current_mileage - self.last_service_mileage) > self.willoughby_milage_need_service:
            return True
        else: return False