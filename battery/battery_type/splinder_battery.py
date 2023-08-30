from battery.battery import Battery

class SplinderBattery(Battery):
    def __init__(self, last_service_date,current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    def needs_service(self):
        service_year = self.last_service_date.year + 2
        current_year = self.current_date.year
        if(current_year>=service_year):
            return True
        else: return False