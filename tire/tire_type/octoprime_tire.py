from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, arr):
        self.arr = arr

    def needs_service(self):
        sumLimit = 3
        __sumOfTiresArray = sum(self.arr)
        if __sumOfTiresArray >= sumLimit:
            return True
        else:
            return False
