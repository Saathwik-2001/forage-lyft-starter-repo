from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self,arr):
        self.arr = arr

    def needs_service(self):
        limit = 0.9
        if (self.arr[0] >= limit or self.arr[1] >= limit or self.arr[2] >= limit or self.arr[3] >= limit):
            return True
        else:
            return False